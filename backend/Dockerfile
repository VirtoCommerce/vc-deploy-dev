FROM mcr.microsoft.com/dotnet/aspnet:8.0

COPY ./backend/platform /opt/virtocommerce/platform

RUN apt-get update && apt-get install -y wget fontconfig libfreetype6 libx11-6 libxcb1 libxext6 libxrender1 xfonts-75dpi xfonts-base libjpeg62-turbo libssl3=3.0.* \
  && wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_amd64.deb \
  && dpkg -i wkhtmltox_0.12.6.1-3.bookworm_amd64.deb

RUN apt-get clean autoclean \
    && apt-get autoremove --yes \
    && rm -rf /var/lib/{apt,dpkg,cache,log}/
WORKDIR /opt/virtocommerce/platform

EXPOSE 80
ENV ASPNETCORE_HTTP_PORTS=80
ENTRYPOINT ["dotnet", "VirtoCommerce.Platform.Web.dll"]
#
