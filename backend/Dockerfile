ARG PLATFORM_IMAGE=ghcr.io/virtocommerce/platform
ARG PLATFORM_TAG=linux-latest
FROM $PLATFORM_IMAGE:$PLATFORM_TAG

ENV APP_USER virto
RUN groupadd -g 1500 $APP_USER && \
	useradd -r $APP_USER -g 1500 -u 1500

COPY ./platform /opt/virtocommerce/platform

USER $APP_USER

WORKDIR /opt/virtocommerce/platform

EXPOSE 8080

ENTRYPOINT ["dotnet", "VirtoCommerce.Platform.Web.dll"]
#