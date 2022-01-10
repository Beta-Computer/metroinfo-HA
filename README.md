# Metroinfo-HA
Connect metroinfo api to Home assistant

1. get api token from [here](https://apidevelopers.metroinfo.co.nz)
<p class='img'>
  <img src='/images/Metroinfo-dev-webiste.jpeg' alt='Screenshot of the metroinfo Developer portal'>
  Click on sign up.
</p>

2. enter your details
3. Add ['metroinfo.py'](/config/metroinfo.py) to your config folder.
4. open metroinfo.py with [Visual Studio Code](https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_vscode), [File editor](https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_configurator) or [Samba share](https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_samba)
5. change apitoken to your api token.
6. change stopcode to a stop found [here](https://go.metroinfo.co.nz/) 
7. change the filter bus code. list of bus route codes can be found [here](/metroinfo-data/routes.txt)
8. Open `configuration.yaml` and add this code. See [this](https://www.home-assistant.io/docs/configuration/#editing-configurationyaml) if you need help editing `configuration.yaml`

```yaml
- platform: command_line
  name: Bus Time
  command: "python3 metroinfo.py"
```

[Restart Home assistant](https://www.home-assistant.io/docs/configuration/#reloading-changes) 

<a href="https://my.home-assistant.io/redirect/server_controls/" target="_blank"><img src="https://my.home-assistant.io/badges/server_controls.svg" alt="Open your Home Assistant instance and show your server controls." /></a>
