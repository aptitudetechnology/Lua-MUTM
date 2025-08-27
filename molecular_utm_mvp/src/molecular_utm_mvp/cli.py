#!/usr/bin/env python3
"""
Command-line interface for Molecular UTM MVP
"""

import click
import asyncio
import sys
from pathlib import Path

from .core import MolecularUTM, UTMConfig
from .benchmarks import run_benchmark_suite


@click.group()
@click.option('--debug/--no-debug', default=False, help='Enable debug mode')
@click.option('--config', type=click.Path(exists=True), help='Configuration file path')
@click.pass_context
def main(ctx, debug, config):
    """Molecular Universal Turing Machine MVP CLI"""
    ctx.ensure_object(dict)
    ctx.obj['debug'] = debug
    ctx.obj['config'] = config


@main.command()
@click.argument('crn_file', type=click.Path(exists=True))
@click.option('--async-mode/--sync-mode', default=False, help='Execution mode')
@click.pass_context
def run_crn(ctx, crn_file, async_mode):
    """Execute a Chemical Reaction Network file"""
    config = UTMConfig(debug_mode=ctx.obj['debug'])
    utm = MolecularUTM(config)
    
    if async_mode:
        asyncio.run(utm.execute_crn_async(crn_file))
    else:
        utm.execute_crn_sync(crn_file)


@main.command()
@click.option('--problem', type=click.Choice(['tsp', '3sat', 'all']), default='all')
@click.option('--size', type=int, default=10, help='Problem size')
@click.pass_context
def benchmark(ctx, problem, size):
    """Run benchmark suite"""
    run_benchmark_suite(problem, size, debug=ctx.obj['debug'])


@main.command()
def workers():
    """List available molecular workers"""
    from .workers import WorkerRegistry
    registry = WorkerRegistry()
    
    click.echo("Available Molecular Workers:")
    for worker_name, worker_class in registry.list_workers():
        click.echo(f"  - {worker_name}: {worker_class.__doc__ or 'No description'}")


if __name__ == '__main__':
    main()
