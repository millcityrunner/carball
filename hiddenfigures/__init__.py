try:
    from hiddenfigures.decompile_replays import decompile_replay
    from hiddenfigures.decompile_replays import analyze_replay_file
except ModuleNotFoundError as e:
    print("Not importing functions due to missing packages:", e)