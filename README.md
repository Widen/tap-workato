# tap-workato

`tap-workato` is a Singer tap for Workato.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation
This tap is installable via pypi

```bash
pipx install tap-workato
```

## Configuration

### Accepted Config Options

- [ ] `Developer TODO:` Provide a list of config options accepted by the tap.

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-workato --about
```

### Source Authentication and Authorization

- [ ] `Developer TODO:` If your tap requires special access on the source system, or any special authentication requirements, provide those here.

## Usage

You can easily run `tap-workato` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-workato --version
tap-workato --help
tap-workato --config CONFIG --discover > ./catalog.json
```

## Developer Resources

- [ ] `Developer TODO:` As a first step, scan the entire project for the text "`TODO:`" and complete any recommended steps, deleting the "TODO" references once completed.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_workato/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-workato` CLI interface directly using `poetry run`:

```bash
poetry run tap-workato --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-workato
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-workato --version
# OR run a test `elt` pipeline:
meltano elt tap-workato target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
