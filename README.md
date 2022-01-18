# Metroinfo-HA
Connect Metroinfo api to Home assistant

## Setup


1. Get your own api token from [https://apidevelopers.metroinfo.co.nz](https://apidevelopers.metroinfo.co.nz)
<p class='img'>
  <img src='/images/Metroinfo-dev-webiste.jpeg' alt='Screenshot of the metroinfo Developer portal'>
  Click on sign up.
</p>

2. Enter your details
3. Go to your email and click the link sent to you by metroinfo
4. Sign in with your email and password
5. subscribe to [real time information](https://apidevelopers.metroinfo.co.nz/product#product=real-time-information)
<p class='img'>
  <img src='images/Products.png' alt='Screenshot of the metroinfo Products portal'>
</p>
6. Name it something recognisable for example "home assistant", agree to the terms and conditions and click subscribe
<p class='img'>
  <img src='images/Subscribe-page-screenshot.png' alt='Screenshot of the metroinfo Products portal'>
</p>

7. Write down your api token. 
8. Add `metroinfo.py` and `Setup.py` to the same folder as your `configuration.yaml`. These can be found [here.](/config/)
9. Open `Setup.py` with [Visual Studio Code](https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_vscode), [File editor](https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_configurator) or [Samba share](https://my.home-assistant.io/redirect/supervisor_addon/?addon=core_samba)

10. Change `apitoken` to your api token. Api token can be found [here](https://apidevelopers.metroinfo.co.nz/profile)
11. Change `stopcode` to a stop found [here.](https://go.metroinfo.co.nz/) List of stop codes can be found [here](/metroinfo-data/stops.txt)
12. Change `filterbuscode`. list of bus route codes can be found [here](/metroinfo-data/routes.txt)

If you want to get the next bus regardless of the next bus code use this in `Setup.py`

```python
apitoken = "paste your api token here"
stopcode = "53088"
filterbuscode = 0
```
If you would like to filter by a bus code for example: "29" use this in `Setup.py`
```python
apitoken = "paste your api token here"
stopcode = "53088"
filterbuscode = '29'
```

13. Open `configuration.yaml` and add this code. See [this](https://www.home-assistant.io/docs/configuration/#editing-configurationyaml) if you need help editing `configuration.yaml`
```yaml
- platform: command_line
  name: Bus Time
  command: "python3 metroinfo.py"
```

14. [Restart Home assistant](https://www.home-assistant.io/docs/configuration/#reloading-changes) 




<a href="https://my.home-assistant.io/redirect/server_controls/" target="_blank"><img src="https://my.home-assistant.io/badges/server_controls.svg" alt="Open your Home Assistant instance and show your server controls." /></a>

## Troubleshooting
### IndexError: list index out of range
  
  - Make sure filter bus code is a string for example `filterbuscode = '5'` or set `filterbuscode = 0` if you would like to get the next bus regartless of code.
  - You may get this error if a bus is not scheduled at this stop.

### Other Error
  - [Open a issue](https://github.com/Beta-Computer/metroinfo-HA/issues/new/choose)
