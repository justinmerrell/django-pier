<div align="center">

<h1>pier</h1>

[![CodeQL](https://github.com/justinmerrell/pier/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/justinmerrell/pier/actions/workflows/codeql-analysis.yml)

</div>

## Motivation

As developers we aim to avoid writting the same code over and over again; and yet we continute to dread starting a new project because of all those setup tasks we think we will only have to do once.

Django already does all of the heavy lifting for us.... after it is installed. The goal with django-pier is to elliminate that gap between starring at a blank screen and writting code for a specific project.

Similar to other PaaS solutions, django-pier will provide you with a high level overview of all of your projects and a clear checklist of what needs done from a DevOps standpoint to maximise your productivity.

### Scope

While the project is tightly integrated with Digital Ocean as the primary hosting provider, pull requests are welcome to add support for other hosting providers using the same methodoligies.

- Launching Digital Ocean droplets
- Launching Digital Ocean hosted databases
- Establishing a Development and Production Environment

The states of the projects are all pulled via API calls to ensure the dashboard reflects on realtime data.

## Getting Started

This project relies heavily on [django-DevOps](https://github.com/justinmerrell/django-DevOps) to provide consistancy between all deployed projects.
