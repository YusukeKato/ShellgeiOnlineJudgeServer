#!/usr/bin/env python3
import sys, subprocess
import asyncio
import time
import timeout_decorator
sys.path.append('/home/ec2-user/.local/lib/python3.9/site-packages/timeout_decorator')

@timeout_decorator.timeout(3)
async def main(cid):
  try:
    result = await asyncio.wait_for(shellgei(cid), timeout=3)
    print(result)
  except asyncio.TimeoutError:
    print("!!time out!!")

@timeout_decorator.timeout(3)
async def shellgei(cid):
  result = subprocess.run(['sudo', 'docker', 'exec', '--user', '1000', cid, '/bin/bash', '-c','./z.bash'], encoding='utf-8', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  return result.stdout

args = sys.argv
cid = args[1]
asyncio.run(main(cid))
