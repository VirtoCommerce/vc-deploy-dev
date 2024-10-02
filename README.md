# Overview
Initial GitOps template for Virto Cloud.

## Features 
* GitOps repository structure for Virto Commerce Platform and Virto Cloud infrastructure.
* GitHub workflows for automatic deployment of Virto Commerce Platform and Virto Cloud infrastructure.

## Folder structure
* **.github/workflows** - GitHub workflows folder with trigger on commit to the main branch.
	* **deploy-backend.yml** - GitHub workflow with Cloud platform deployment actions.
	* **deploy-infra.yml** - GitHub workflow with Cloud infra deployment actions.
* **backend** - Virto Commerce Platform deployment.
	* **packages.json** - defines version of Virto Commerce Platform and modules.
	* **Dockerfile** - Dockerfile for Virto Commerce Platform deployment.
* **infra** - declarative description of Virto Cloud infrastructure deployment.
	* environment.yml
	

## How to use

### Pre-requirements
1. Access to Virto Cloud Portal.
1. Create and deploy new environment in Virto Cloud Portal.
1. Download environment manifest from Virto Cloud Portal.
1. Create API Key in Virto Cloud Portal (PLATFORM_TOKEN).
1. DOCKER_LOGIN
1. DOCKER_PASSWORD
1. Enable GitOps in Virto Cloud Portal for the environment.


### GitHub repository setup
1. Create a new repository in your GitHub account.
1. Copy content of from this branch to your repository.

### Cloud infrastucture deployment
1. Download environment manifest from Virto Cloud and put it to the **infra** folder.

If you use environment.yml from this repository, you need to replace the following placeholders:
1. Replace TODO_YOUR_ENVIRONMENT_NAME with your environment name in the **environment.yml** file.
1. Replace TODO_YOUR_FRONTEND_HOSTNAME with your frontend hostname in the **environment.yml** file.
1. Replace TODO_YOUR_STORE_ID with your store id in the **environment.yml** file.

### Virto Commerce Platform deployment
1. Update **packages.json** file with the required version of Virto Commerce Platform and modules.
1. Set DOCKER_LOGIN in deploy-backend.yml

### GitHub Actions
1. Go to the **Settings** tab of your repository.
1. Go to the **Secrets** section.
1. Add VIRTOSTART_ACR_DOCKER_PASSWORD and VIRTOSTART_PLATFORM_TOKEN secrets.

## Do Commit to the main branch
1. Commit changes to the main branch.
1. Review GitHub Actions logs.
1. Review Virto Cloud Portal logs.



