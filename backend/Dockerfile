FROM mcr.microsoft.com/dotnet/aspnet:8.0

COPY ./backend/platform /opt/virtocommerce/platform
COPY ./backend/YamlDotNet.dll /opt/virtocommerce/platform/app_data/modules

RUN apt-get update && apt-get install -y wget fontconfig libfreetype6 libx11-6 libxcb1 libxext6 libxrender1 xfonts-75dpi xfonts-base libjpeg62-turbo

RUN apt-get clean autoclean \
    && apt-get autoremove --yes \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/
WORKDIR /opt/virtocommerce/platform

ENTRYPOINT ["dotnet", "VirtoCommerce.Platform.Web.dll"]
#
