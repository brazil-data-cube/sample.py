#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2020-20201 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Command line interface for the SampleDB client."""

import click

from .sample import SAMPLE


class Config:
    """A simple decorator class for command line options."""

    def __init__(self):
        """Initialize of Config decorator."""
        self.url = None
        self.service = None
        self.lccs_url = None
        self.access_token = None


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--url', default='http://127.0.0.1:5000/',
              help='The Sample-WS address (an URL).')
@click.option('--access-token', default=None, help='Personal Access Token of the BDC Auth')
@click.option('--lccs_url', type=click.STRING, default='https://brazildatacube.dpi.inpe.br/lccs',
              help='The LCCS-WS address (an URL).')
@click.version_option()
@pass_config
def cli(config, url, lccs_url, access_token=None):
    """Sample on command line."""
    config.url = url
    config.service = SAMPLE(url=url, access_token=access_token, lccs_url=lccs_url)


@cli.command()
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def datasets(config: Config, verbose):
    """List available datasets."""
    if verbose:
        click.secho(f'WFS: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving the list of available datasets... ',
                    bold=False, fg='black')

        for ds in config.service.datasets:
            click.secho(f'\t\t- {ds}', bold=True, fg='green')

        click.secho('\tFinished!', bold=False, fg='black')

    else:
        for ds in config.service.datasets:
            click.secho(f'{ds}', bold=True, fg='green')


@cli.command()
@click.option('--dataset_id', default=None, type=click.STRING, required=False,
              help='The dataset id to return information.')
@click.option('--dataset_name', default=None, type=click.STRING, required=False,
              help='The dataset name to return information.')
@click.option('--dataset_version', default=None, type=click.STRING, required=False,
              help='The dataset version to return information.')
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def describe_dataset(config: Config, dataset_id, dataset_name, dataset_version, verbose):
    """Retrieve information of a specific dataset."""
    if dataset_id:
        retval = config.service.dataset(dataset_id=dataset_id)
    elif dataset_name is not None and dataset_version is not None:
        retval = config.service.dataset(dataset_name=dataset_name, dataset_version=dataset_version)
    else:
        click.secho('You must enter the dataset identifier or its name and version !',
                    bold=True, fg='red')
        return

    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving the describe of dataset... ',
                    bold=False, fg='black')

        click.secho(f'\t- {retval}', bold=True, fg='green')

        click.secho('\tFinished!', bold=False, fg='black')

    else:
        click.secho(f'{retval}', fg='green')


@cli.command()
@click.option('--dataset_id', default=None, type=click.STRING, required=False,
              help='The dataset id to return information.')
@click.option('--dataset_name', default=None, type=click.STRING, required=False,
              help='The dataset name to return information.')
@click.option('--dataset_version', default=None, type=click.STRING, required=False,
              help='The dataset version to return information.')
@click.option('--filename', type=click.STRING, required=True, help='File path or file handle to write to')
@click.option('--limit', default=None, type=click.INT,
              help='The maximum number of results to return (page size). Defaults to None')
@click.option('--page', default=None, type=click.INT, help='The page number of results..')
@click.option('--driver', type=click.STRING, required=False, default='ESRI Shapefile',
              help='The OGR format driver used to write the vector file')
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def export_data(config: Config, dataset_id, dataset_name, dataset_version, limit, page, filename, driver, verbose):
    """Save dataset data of a specific dataset."""
    if dataset_id:
        retval = config.service.dataset(dataset_id=dataset_id)
    elif dataset_name is not None and dataset_version is not None:
        retval = config.service.dataset(dataset_name=dataset_name, dataset_version=dataset_version)
    else:
        click.secho('You must enter the dataset identifier or its name and version !',
                    bold=True, fg='red')
        return

    filter = {
        'limit': limit,
        'page': page
    }

    gdf = retval.data(filter=filter)

    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tSave dataset data..',
                    bold=False, fg='black')

        config.service.save_feature(filename, gdf, driver)

        click.secho(f'\t- Saved dataset in {filename}', bold=True, fg='green')

        click.secho('\tFinished!', bold=False, fg='black')

    else:
        config.service.save_feature(filename, gdf, driver)

        click.secho(f'Saved dataset in {filename}', fg='green')

