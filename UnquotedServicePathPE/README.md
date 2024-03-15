# Unquoted Service Path Escalation. 

Windows services that do not have fully quoted paths can be exploited if there Service Binary's path location contains
1. White Space
2. Folder is writable. 

This little script currently, only details the Services with unquoted service paths. 