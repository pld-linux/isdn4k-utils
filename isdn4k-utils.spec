%define Version 2.1b1

Summary     	: Utilities for the kernel ISDN-subsystem.
Name        	: isdn4k-utils
Version     	: %{Version}
Release     	: 6
Group       	: Communication/ISDN
Copyright   	: distributable
Packager    	: rf@lst.de (Ralf Flaxa)
URL         	: http://www.franken.de/ftp/pub/isdn4linux/
BuildRoot   	: /tmp/isdn4k-utils-%{Version}

Source0: ftp://ftp.franken.de/pub/isdn4linux/v2.1/isdn4k-utils-%{Version}.tar.gz
Source1: isdn4k-utils-%{Version}.config
Patch0: isdn4k-utils-%{Version}-COL.patch


%Description
Utilities for the kernel ISDN-subsystem and some contributions.


%Prep
%setup
%patch -P 0 -p1
cp -p $RPM_SOURCE_DIR/isdn4k-utils-%{Version}.config .config


%Build
make OPTIM="$RPM_OPT_FLAGS" oldconfig
make CFLAGS="$RPM_OPT_FLAGS"


%Install
DESTDIR=$RPM_BUILD_ROOT; export DESTDIR
[ -n "`echo $DESTDIR | sed -n 's:^/tmp/[^.].*$:OK:p'`" ] && rm -rf $DESTDIR ||
(echo "Invalid BuildRoot: '$DESTDIR'! Check this .spec ..."; exit 1) || exit 1

make devices

mkdir -p $DESTDIR/etc/isdn
mkdir -p $DESTDIR/sbin
mkdir -p $DESTDIR/usr/X11R6/lib/app-defaults
mkdir -p $DESTDIR/usr/bin
mkdir -p $DESTDIR/usr/doc/faq/isdn4linux
mkdir -p $DESTDIR/var/lock/isdn

make install

cp -a isdnlog/isdnrep/isdnrep.1 ${DESTDIR}/usr/man/man1
cp -a isdnlog/isdnlog/isdnlog.8 ${DESTDIR}/usr/man/man8
ln -sf ttyI.4 ${DESTDIR}/usr/man/man4/cui.4

strip $DESTDIR/sbin/avmcapictrl
strip $DESTDIR/sbin/hisaxctrl
strip $DESTDIR/sbin/icnctrl
strip $DESTDIR/sbin/imon
strip $DESTDIR/sbin/imontty
strip $DESTDIR/sbin/ipppd
strip $DESTDIR/sbin/ipppstats
strip $DESTDIR/sbin/iprofd
strip $DESTDIR/sbin/isdnctrl
strip $DESTDIR/sbin/isdnlog
strip $DESTDIR/sbin/pcbitctl
strip $DESTDIR/usr/bin/isdnconf
strip $DESTDIR/usr/bin/isdnrep
strip $DESTDIR/usr/bin/xisdnload
strip $DESTDIR/usr/bin/xmonisdn

# gzip man pages and fix sym-links
MANPATHS=`find $DESTDIR -type d -name "man[1-9n]" -print`
if [ -n "$MANPATHS" ]; then
  chown -Rvc root.root $MANPATHS
  find $MANPATHS -type l -print |
    perl -lne '($f=readlink($_))&&unlink($_)&&symlink("$f.gz","$_.gz")||die;'
  find $MANPATHS -type f -print |
    xargs -r gzip -v9nf
fi


%Clean
DESTDIR=$RPM_BUILD_ROOT;export DESTDIR;[ -n "$UID" ]&&[ "$UID" -gt 0 ]&&exit 0
[ -n "`echo $DESTDIR | sed -n 's:^/tmp/[^.].*$:OK:p'`" ] && rm -rf $DESTDIR ||
(echo "Invalid BuildRoot: '$DESTDIR'! Check this .spec ..."; exit 1) || exit 1


%Files
%doc COPYING README
%dir /usr/doc/faq/isdn4linux
/usr/doc/faq/isdn4linux/de-i4l-faq.asc
/usr/doc/faq/isdn4linux/de-i4l-faq.html
/usr/doc/faq/isdn4linux/eng-i4l-faq.asc
/usr/doc/faq/isdn4linux/eng-i4l-faq.html

%dir /var/lock/isdn

%dir /etc/isdn
%config /etc/isdn/callerid.conf
%config /etc/isdn/isdn.conf

/dev/*

/sbin/avmcapictrl
/sbin/hisaxctrl
/sbin/icnctrl
/sbin/imon
/sbin/imontty
/sbin/ipppd
/sbin/ipppstats
/sbin/iprofd
/sbin/isdnctrl
/sbin/isdnlog
/sbin/pcbitctl
/sbin/telesctrl

/usr/X11R6/lib/X11/app-defaults/XISDNLoad

/usr/bin/isdnconf
/usr/bin/isdnrep
/usr/bin/xisdnload
/usr/bin/xmonisdn

%dir /usr/lib/isdn
/usr/lib/isdn/areacodes

/usr/lib/vbox

/usr/man/man1/isdnrep.1*
/usr/man/man1/xisdnload.1x*
/usr/man/man1/xmonisdn.1x*
/usr/man/man4/cui.4*
/usr/man/man4/ttyI.4*
/usr/man/man4/isdninfo.4*
/usr/man/man4/isdn_audio.4*
/usr/man/man7/isdn_cause.7*
/usr/man/man8/avmcapictrl.8*
/usr/man/man8/hisaxctrl.8*
/usr/man/man8/icnctrl.8*
/usr/man/man8/imon.8*
/usr/man/man8/ipppd.8*
/usr/man/man8/ipppstats.8*
/usr/man/man8/iprofd.8*
/usr/man/man8/isdnctrl.8*
/usr/man/man8/telesctrl.8*


%ChangeLog
* Mon Jan 01 1997 ...

$Id: isdn4k-utils.spec,v 1.1 1999-07-16 21:35:36 kloczek Exp $
