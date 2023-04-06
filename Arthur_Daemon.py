from Arthur_Bot import run
import daemon


with daemon.DaemonContext():
    run(TOKEN)

