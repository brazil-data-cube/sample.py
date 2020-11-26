#
# This file is part of Python Client Library for SampleDB.
# Copyright (C) 2019 INPE.
#
# Python Client Library for SampleDB is free software; you can redistribute it and/or modify it
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
        self.auth = None


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--url', type=click.STRING, default='http://localhost',
              help='The GeoServer address (an URL).')
@click.option('--user', type=click.STRING, default='reader',
              help='The user of server address.')
@click.option('--password', prompt=True, hide_input=True, default=None, help='The password of server address.')
@pass_config
def cli(config, url, user, password):
    """Sample on command line."""
    config.url = url
    config.auth = (user, password)


@cli.command()
@click.option('-v', '--verbose', is_flag=True, default=False)
@pass_config
def datasets(config, verbose):
    """List available datasets."""
    if verbose:
        click.secho(f'WFS: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving the list of available datasets... ',
                    bold=False, fg='black')
    s = SAMPLE(wfs=config.url, auth=config.auth)

    if verbose:
        for ds in s.datasets:
            click.secho(f'\t\t- {ds}', bold=True, fg='green')
    else:
        for ds in s.datasets:
            click.secho(f'{ds}', bold=True, fg='green')

    if verbose:
        click.secho('\tFinished!', bold=False, fg='black')


@cli.command()
@pass_config
@click.argument('name', type=click.STRING, required=False)
@click.option('-v', '--verbose', is_flag=True, default=False)
def describe_dataset(config, name, verbose):
    """Describe dataset giving a dataset name."""
    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving the describe of dataset... ',
                    bold=False, fg='black')

    s = SAMPLE(wfs=config.url, auth=config.auth)

    retval = s.dataset(name)

    click.secho(f'\t- {retval}', bold=True, fg='green')

    if verbose:
        click.secho('\tFinished!', bold=False, fg='black')


@cli.command()
@pass_config
@click.argument('name', type=click.STRING, required=False)
@click.option('-v', '--verbose', is_flag=True, default=False)
def dataset_metadata(config, name, verbose):
    """Retrieve the dataset metadata."""
    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tRetrieving the dataset metadata... ',
                    bold=False, fg='black')
    s = SAMPLE(wfs=config.url, auth=config.auth)

    retval = s.dataset(name)

    click.secho(f'\t- {retval}', bold=True, fg='green')

    if verbose:
        click.secho('\tFinished!', bold=False, fg='black')


@cli.command()
@pass_config
@click.argument('name', type=click.STRING, required=True)
@click.option('--filename', type=click.STRING, required=True, help='File path or file handle to write to')
@click.option('--driver', type=click.STRING, required=False, default='ESRI Shapefile',
              help='The OGR format driver used to write the vector file')
@click.option('-v', '--verbose', is_flag=True, default=False)
def save_observations(config, name, filename, driver, verbose):
    """Save observations giving observation name."""
    if verbose:
        click.secho(f'Server: {config.url}', bold=True, fg='black')
        click.secho('\tSave dataset obserservation ',
                    bold=False, fg='black')

    s = SAMPLE(wfs=config.url, auth=config.auth)

    gdf = s.dataset(name).observation

    s.save_feature(filename, gdf, driver)

    pprint("Observation {} save in {}!".format(name, filename))

    if verbose:
        click.secho('\tFinished!', bold=False, fg='black')
