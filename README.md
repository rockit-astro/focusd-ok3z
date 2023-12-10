## ASA ok3z Focuser daemon

`focusd` interfaces with and wraps an ASA ok3z focuser and exposes it via Pyro.

`focus` is a commandline utility for controlling the focuser.

### Configuration

Configuration is read from json files that are installed by default to `/etc/focusd`.
A configuration file is specified when launching the server, and the `focus` frontend will search this location when launched.

The configuration options are:
```python
{
  "daemon": "ngts_m06_focuser", # Run the server as this daemon. Daemon types are registered in `rockit.common.daemons`.
  "log_name": "focusd@ngts_m06", # The name to use when writing messages to the observatory log.
  "control_machines": ["NGTSDASNUC"], # Machine names that are allowed to control (rather than just query) state. Machine names are registered in `rockit.common.IP`.
  "serial_port": "/dev/focuser",
  "serial_baud": 38400,
  "serial_timeout": 5,
  "move_timeout": 180,
  "steps_per_mm": 5088,
  "anti_backlash_mm": 0.5,
  "focus_range_mm": 6.0,
  "speed_mm_sec": 0.5,
  "acceleration_mm_sec_sec": 5
}

```
## Initial Installation

The automated packaging scripts will push 4 RPM packages to the observatory package repository:

| Package                     | Description                                                                  |
|-----------------------------|------------------------------------------------------------------------------|
| rockit-focuser-ok3z-server  | Contains the `focusd` server and systemd service file.                       |
| rockit-focuser-ok3z-client  | Contains the `focus` commandline utility for controlling the focuser server. |
| python3-rockit-focuser-ok3z | Contains the python module with shared code.                                 |
| rockit-atlas-data-ngts-m06  | Contains the json configuration for NGTS M06.                                |

After installing packages, the systemd service should be enabled:

```
sudo systemctl enable --now focusd@<config>
```

where `config` is the name of the json file for the appropriate telescope.

Now open a port in the firewall:
```
sudo firewall-cmd --zone=public --add-port=<port>/tcp --permanent
sudo firewall-cmd --reload
```
where `port` is the port defined in `rockit.common.daemons` for the daemon specified in the config.

### Upgrading Installation

New RPM packages are automatically created and pushed to the package repository for each push to the `master` branch.
These can be upgraded locally using the standard system update procedure:
```
sudo yum clean expire-cache
sudo yum update
```

The daemon should then be restarted to use the newly installed code:
```
sudo systemctl restart focusd@<config>
```

### Testing Locally

The camera server and client can be run directly from a git clone:
```
./focusd test.json
FOCUSD_CONFIG_PATH=./ngts_m06.json ./focus status
```
