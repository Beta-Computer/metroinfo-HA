# Metroinfo-HA
Connect metroinfo api to Home assistant

You will need to edit your `configuration.yaml` see [this](https://www.home-assistant.io/docs/configuration/) if you need help

1. get api token from [here](https://apidevelopers.metroinfo.co.nz)
2. Add metroinfo.py to your config folder
3. Open 'configuration.yaml' and add this code
```yaml
- platform: command_line
  name: Bus Time
  command: "python3 metroinfo.py"
```
3. change stopcode to a stop found [here](https://go.metroinfo.co.nz/) 
