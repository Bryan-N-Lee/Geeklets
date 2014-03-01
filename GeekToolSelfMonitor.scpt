-- The Memory Threshold in MB
set mem_limit to 100

set app_name to "GeekTool"
set the_pid to (do shell script "ps ax | grep " & (quoted form of app_name) & " | grep -v grep | awk '{print $1}' | head -n 1")
set mem_use to (do shell script "ps -xo 'rss,ucomm' | sort -nr | awk '/GeekTool/ {printf \"%.2f\\n\", $1/1024}' | head -n 1")

if mem_limit - mem_use < 0 then
  do shell script ("kill -9 " & the_pid)
	do shell script "open '/Applications/GeekTool.app'"
end if
set output to mem_use & "MB" & "/" & mem_limit & "MB"
