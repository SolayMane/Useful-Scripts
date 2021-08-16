## How to mount a hard disk > 2T on linux
```` bash
fdisk -l ## to list disks
parted /dev/targetdisk/ print
#you will get like this results:
Model: Seagate BUP RD (scsi)
Disk /dev/sdw: 5001GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt

Number  Start   End     Size    File system  Name                          Flags
 1      17,4kB  134MB   134MB                Microsoft reserved partition  msftres
 2      135MB   3426GB  3426GB  ntfs         Basic data partition          msftdata
 3      3426GB  5001GB  1575GB  ntfs         Basic data partition          msftdata
#To mount the second partition, use the mount command in the same way you usually would.
mount -t xfs /dev/sdw2 /mnt/test
``
