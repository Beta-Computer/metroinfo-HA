# Metroinfo-HA
Connect metroinfo api to Home assistant

1. Get your own api token from [here](https://apidevelopers.metroinfo.co.nz)
<p class='img'>
  <img src='/images/Metroinfo-dev-webiste.jpeg' alt='Screenshot of the metroinfo Developer portal'>
  Click on sign up.
</p>

2. Enter your details
3. Write down your api token.
4. Add 'metroinfo.py' to the same folder as your `configuration.yaml`. 'metroinfo.py' can be found [here](/config/metroinfo.py)
5. open metroinfo.py with [Visual Studio Code](https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_vscode), [File editor](https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_configurator) or [Samba share](https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_samba)
6. change apitoken to your api token. Api token Can be found [here](https://apidevelopers.metroinfo.co.nz/profile)
7. change stopcode to a stop found [here.](https://go.metroinfo.co.nz/) List of stop codes can be found [here](/metroinfo-data/stops.txt)
8. change the filter bus code. list of bus route codes can be found [here](/metroinfo-data/routes.txt)
9. Open `configuration.yaml` and add this code. See [this](https://www.home-assistant.io/docs/configuration/#editing-configurationyaml) if you need help editing `configuration.yaml`
```yaml
- platform: command_line
  name: Bus Time
  command: "python3 metroinfo.py"
```

10. [Restart Home assistant](https://www.home-assistant.io/docs/configuration/#reloading-changes) 




<a href="https://my.home-assistant.io/redirect/server_controls/" target="_blank"><img src="https://my.home-assistant.io/badges/server_controls.svg" alt="Open your Home Assistant instance and show your server controls." /></a>
