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

from .sample import sample


class Config:
    """A simple decorator class for command line options."""

    def __init__(self):
        """Initialize of Config decorator."""
        self.url = None
        self.auth = None


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--url', type=click.STRING, default='http://localhost',
              help='The WLTS server address (an URL).')
@click.option('--user', type=click.STRING, default='admin',
              help='The user of server address.')
@click.option('--password', prompt=True, hide_input=True,default=None, help='The password of server address.')
@pass_config
def cli(config, url, user, password):
    """Sampledb on command line."""
    config.url = url
    config.auth = (user, password)

@cli.command()
@pass_config
def datasets(config):
    """List All Datasets Avaliables."""
    s = sample(wfs=config.url, auth=config.auth)

    pprint(s.datasets())


@cli.command()
@pass_config
@click.argument('name', type=click.STRING, required=False)
def describe_dataset(config, name):
    """Describe dataset giving a dataset name."""
    s = sample(wfs=config.url, auth=config.auth)

    retval = s.describe_dataset(name)

    del retval['metadata_json']

    pprint(retval)

@cli.command()
@pass_config
@click.argument('name', type=click.STRING, required=False)
def dataset_metadata(config, name):
    """Retrive a Metadata Json from dataseet."""
    s = sample(wfs=config.url, auth=config.auth)

    retval = s.describe_dataset(name)

    pprint(retval['metadata_json'])

@cli.command()
@pass_config
@click.argument('name', type=click.STRING, required=False)
def get_observations(config, name):
    """Retrive a Metadata Json from dataseet."""
    s = sample(wfs=config.url, auth=config.auth)

    retval = s.get_observation(name)

    pprint(retval)