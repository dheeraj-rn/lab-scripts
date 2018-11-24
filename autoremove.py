#!/usr/bin/env python3
#https://github.com/dheeraj-rn
import asyncio, asyncssh

async def run_client(host, command):
#    async with asyncssh.connect(host, username='username', password='password') as conn:
     async with asyncssh.connect(host, username='username') as conn:
         return await conn.run(command)

async def run_multiple_clients():
    # Put your lists of hosts here
    hosts = ['192.168.1.11', '192.168.1.12', '192.168.1.13', '192.168.1.14', '192.168.1.15', '192.168.1.16', '192.168.1.17', '192.168.1.18', '192.168.1.19', '192.168.1.21', '192.168.1.22', '192.168.1.23', '192.168.1.24', '192.168.1.25', '192.168.1.26', '192.168.1.27', '192.168.1.28', '192.168.1.29', '192.168.1.30', '192.168.1.31', '192.168.1.32', '192.168.1.33', '192.168.1.34', '192.168.1.35', '192.168.1.36', '192.168.1.37', '192.168.1.38', '192.168.1.39', '192.168.1.40', '192.168.1.41', '192.168.1.42', '192.168.1.43', '192.168.1.44', '192.168.1.45', '192.168.1.46', '192.168.1.47', '192.168.1.48', '192.168.1.49', '192.168.1.50', '192.168.1.51', '192.168.1.52', '192.168.1.53', '192.168.1.54', '192.168.1.55', '192.168.1.56', '192.168.1.57', '192.168.1.58', '192.168.1.59', '192.168.1.60', '192.168.1.61', '192.168.1.62', '192.168.1.63', '192.168.1.64', '192.168.1.65', '192.168.1.66', '192.168.1.67', '192.168.1.68', '192.168.1.69', '192.168.1.70', '192.168.1.71', '192.168.1.72', '192.168.1.73', '192.168.1.74', '192.168.1.75', '192.168.1.76', '192.168.1.77', '192.168.1.78', '192.168.1.79', '192.168.1.80', '192.168.1.81', '192.168.1.82', '192.168.1.83', '192.168.1.84', '192.168.1.85']

    tasks = (run_client(host, "echo 'password' | sudo -S apt autoremove -y") for host in hosts)
    results = await asyncio.gather(*tasks, return_exceptions=True)
    #print(results)
    for i, result in enumerate(results, 1):
     try:
        if isinstance(result, Exception):
            print('Task %d failed: %s' % (i, str(result)))
        #elif result.stdout is None:
        else:
            print('Task %d : %s' % (i, str(result.stdout)))
     except Exception as e:
        print(e)
#        print(75*'-')

asyncio.get_event_loop().run_until_complete(run_multiple_clients())
