ARG PLATFORM_IMAGE=ghcr.io/virtocommerce/platform
ARG PLATFORM_TAG=linux-latest
FROM $PLATFORM_IMAGE:$PLATFORM_TAG

COPY ./platform /opt/virtocommerce/platform

WORKDIR /opt/virtocommerce/platform

ENTRYPOINT ["dotnet", "VirtoCommerce.Platform.Web.dll"]
#