# offline_oddo_api

## the problem
* 2 apps one offline and other hosted online, when the offline has internet access send the data to the online (both oddo apps)

https://pypi.org/project/Flask-Odoo/



* https://hub.packtpub.com/building-your-first-odoo-application/


### check connection function
* simple get request to google if response.status_code == 200 (there is internet)
* if response.status_code != 200 ( no internet)
* or https://www.codespeedy.com/how-to-check-the-internet-connection-in-python/


## function to reapeat the connection checkup

* https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds
```
import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print("Doing stuff...")
    # do your stuff
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()
```

## contacts odoo (work with API)

### create new recored in odoo 
```
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{ 'name': "Python King", }])
```

### read company

```
models.execute_kw(db, uid, password,'res.partner', 'search_read',[[['is_company', '=', True]]],{'fields': ['name', 'country_id', 'comment'], 'limit': 20})
```

### get company by id I added this

```
models.execute_kw(db, uid, password,'res.partner', 'search_read',[[['id', '=', 58]]],{'fields': ['name', 'country_id', 'comment']})
```

## update recored (single)
```
models.execute_kw(db, uid, password, 'res.partner', 'write', [58, {'name': "Python King1"}])
```

# update multi
[id, {'name':'new name'}] return true , it can update multi recoreds but all take same name

```
models.execute_kw(db, uid, password, 'res.partner', 'write', [[58,48], {'name': "Python King1"}])
```

### get recored name

models.execute_kw(db, uid, password, 'res.partner', 'name_get', [58])


('my own odoo api calls')[https://github.com/MahmoudHegazi/offline_oddo_api/blob/main/myodoo.JPG?raw=true]
