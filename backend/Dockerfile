ARG PLATFORM_IMAGE=ghcr.io/virtocommerce/platform
ARG PLATFORM_TAG=linux-latest
FROM $PLATFORM_IMAGE:$PLATFORM_TAG

COPY ./platform/modules /opt/virtocommerce/platform/modules

WORKDIR /opt/virtocommerce/platform

ENTRYPOINT ["dotnet", "VirtoCommerce.Platform.Web.dll"]