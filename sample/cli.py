#
# This file is part of Python Client Library for Sample Database Model.
# Copyright (C) 2020-20201 INPE.
#
# Python Client Library for Sample Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Command line interface for the SampleDB client."""

from pprint import pprint

import click

from .sample import SAMPLE


class Config:
    """A simple decorator class for command line options."""

    def __init__(self):
        """Initialize of Config decorator."""
        self.url = None
        self.lccs_url = None
        self.auth = None
        self.service = None


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--url', type=click.STRING, default='https://brazildatacube.dpi.inpe.br/bdc/geoserver',
              help='The GeoServer address (an URL).')
@click.option('--lccs_url', type=click.STRING, default='https://brazildatacube.dpi.inpe.br/dev/lccs',
              help='The GeoServer address (an URL).')
@click.option('--user', type=click.STRING, default=None, required=False,
              help='The user of server address.')
@click.option('--password', prompt=True, hide_input=True, default="", help='The password of server address.')
@click.version_option()
@pass_config
def cli(config, url, lccs_url, user, password):
    """Sample on command line."""
    config.url = url
    config.lccs_url = lccs_url
    if user and password:
        config.service = SAMPLE(wfs=config.url, lccs_url=config.lccs_url, auth=(user, password))
    else:
        config.service = SAMPLE(wfs=config.url, lccs_url=config.lccs_url)


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
@click.option('--dataset', type=click.STRING, required=True, help='The dataset to return information.')
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def describe_dataset(config: Config, dataset, verbose):
    """Retrieve information of a specific dataset."""
    retval = config.service[dataset]

    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving the describe of dataset... ',
                    bold=False, fg='black')

        click.secho(f'\t- {retval}', bold=True, fg='green')

        click.secho('\tFinished!', bold=False, fg='black')

    else:
        click.secho(f'{retval}', fg='green')


@cli.command()
@click.option('--dataset', type=click.STRING, required=True, help='The dataset to return metadata.')
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def dataset_metadata(config: Config, dataset, verbose):
    """Retrieve the dataset metadata."""
    retval = config.service[dataset]

    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving the dataset metadata... ',
                    bold=False, fg='black')

        click.secho(f'\t- {retval.metadata}', bold=True, fg='green')

        click.secho('\tFinished!', bold=False, fg='black')

    else:
        click.secho(f'{retval.metadata}', fg='green')


@cli.command()
@click.option('--dataset', type=click.STRING, required=True, help='The dataset.')
@click.option('--filename', type=click.STRING, required=True, help='File path or file handle to write to')
@click.option('--driver', type=click.STRING, required=False, default='ESRI Shapefile',
              help='The OGR format driver used to write the vector file')
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def dataset_save(config: Config, dataset, filename, driver, verbose):
    """Save dataset data of a specific dataset."""
    retval = config.service[dataset]

    gdf = retval.data

    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tSave dataset data..',
                    bold=False, fg='black')

        config.service.save_feature(filename, gdf, driver)

        click.secho(f'\t- Saved {dataset} in {filename}', bold=True, fg='green')

        click.secho('\tFinished!', bold=False, fg='black')

    else:
        config.service.save_feature(filename, gdf, driver)

        click.secho(f'Saved {dataset} in {filename}', fg='green')

