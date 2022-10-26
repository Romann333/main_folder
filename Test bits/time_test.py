import os
from datetime import datetime
import time

start = time.time()
# if not os.path.exists('data'):
#     os.mkdir('data')

# with open("data/page.html", 'w'):
#     file.write(r.text)
time.sleep(2)
cur_date = datetime.now().strftime("%d_%h_%Y, %H:%M")
diff = time.time() - start

print(cur_date)
print(datetime.now())
print(diff)