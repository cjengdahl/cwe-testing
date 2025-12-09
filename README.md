# CWE Testing Repository

Repo for CWE detection and processing testing with GitHub Actions

## Overview

This repository contains example GitHub workflows for integrating [cjengdahl/cwe-action@v1](https://github.com/cjengdahl/cwe-action) with popular security scanners. The examples demonstrate how to extract CWEs from scanner results and process them using the cwe-action.

## Example Workflows

### Available Scanners

This repository includes example workflows for:

- **GitHub Advanced Security (CodeQL)** - `.github/workflows/ghas.yml`
- **Snyk** - `.github/workflows/snyk.yml`

While these examples focus on popular scanners, the cwe-action can work with any scanner that outputs an array of CWEs.

## Installation

To use these workflows in your own repository:

1. **Copy the workflow file** for your scanner from this repository to your `.github/workflows/` directory

2. **Configure the required secrets** in your repository settings:
   - `SECURITY_JOURNEY_API_KEY` - Your Security Journey API key
   - For Snyk: `SNYK_TOKEN` - Your Snyk authentication token
   - For GitHub Advanced Security: `GITHUB_TOKEN` is automatically provided

3. **Adjust the branch triggers** in the workflow file to match your needs:

   ```yaml
   on:
     pull_request:
       branches:
         - main # Change this to your target branch
   ```

4. **Customize scanner settings** as needed for your specific use case

## How It Works

Each workflow follows a two-job pattern:

1. **Scan Job**: Runs the security scanner and extracts CWEs from the results
2. **Process CWEs Job**: Sends the extracted CWEs to the Security Journey API using cwe-action

The cwe-action requires only one input - an array of CWEs. As long as your scanner can produce this format, you can integrate it with the action.

## Requirements

The only requirement for scanner integration is that it outputs an array of CWEs that can be passed to the cwe-action:

```yaml
- name: Process extracted CWEs
  uses: cjengdahl/cwe-action@v1
  with:
    api_url: https://api.securityjourney.dev/integrations
    api_key: ${{ secrets.SECURITY_JOURNEY_API_KEY }}
    cwes: "${{ needs.scan.outputs.cwes }}" # Array of CWE IDs
```
