# Metroinfo-HA
Connect metroinfo api to Home assistant

## setup


1. Get your own api token from [here](https://apidevelopers.metroinfo.co.nz)
<p class='img'>
  <img src='/images/Metroinfo-dev-webiste.jpeg' alt='Screenshot of the metroinfo Developer portal'>
  Click on sign up.
</p>

2. Enter your details
3. Go to your profile
4. Write down your api token. 
5. Add 'metroinfo.py' to the same folder as your `configuration.yaml`. 'metroinfo.py' can be found [here](/config/metroinfo.py)
6. open metroinfo.py with [Visual Studio Code](https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_vscode), [File editor](https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_configurator) or [Samba share](https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_samba)
7. change apitoken to your api token. Api token Can be found [here](https://apidevelopers.metroinfo.co.nz/profile)
8. change stopcode to a stop found [here.](https://go.metroinfo.co.nz/) List of stop codes can be found [here](/metroinfo-data/stops.txt)
9. change the filter bus code. list of bus route codes can be found [here](/metroinfo-data/routes.txt)
10. Open `configuration.yaml` and add this code. See [this](https://www.home-assistant.io/docs/configuration/#editing-configurationyaml) if you need help editing `configuration.yaml`
```yaml
- platform: command_line
  name: Bus Time
  command: "python3 metroinfo.py"
```

10. [Restart Home assistant](https://www.home-assistant.io/docs/configuration/#reloading-changes) 




<a href="https://my.home-assistant.io/redirect/server_controls/" target="_blank"><img src="https://my.home-assistant.io/badges/server_controls.svg" alt="Open your Home Assistant instance and show your server controls." /></a>

## Troubleshooting
### IndexError: list index out of range
  
  - Make sure filter bus code is a string for example `filterbuscode = '5'` or set `filterbuscode = '0'` if you would like to get the next bus regartless of code.
  - You may get this error if a bus is not scheduled at this stop.

### Other Error
  - [Open a issue](https://github.com/Beta-Computer/metroinfo-HA/issues/new/choose)
