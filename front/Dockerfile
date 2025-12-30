# STAGE 1: BUILD
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /app
COPY ./frontend/ /app/
RUN dotnet publish -c Release -o /app/Release

# STAGE 2: RUN
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS run
WORKDIR /runtime
COPY --from=build /app/Release/ /runtime/

EXPOSE 8080
ENTRYPOINT ["dotnet","frontend.dll"]