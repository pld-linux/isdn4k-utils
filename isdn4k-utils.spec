Summary:	Utilities for the kernel ISDN-subsystem.
Summary(pl):	U¿ytki dla podsystemu ISDN j±dra.
Name:		isdn4k-utils
Version:	2.1b1
Release:	6
Group:		Communication/ISDN
Copyright:	distributable
Source0:	ftp://ftp.franken.de/pub/isdn4linux/v2.1/%{name}-%{nersion}.tar.gz
Source1:	isdn4k-utils-%{version}.config
Patch0:		isdn4k-utils-%{version}-COL.patch
URL:		http://www.franken.de/ftp/pub/isdn4linux/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for the kernel ISDN-subsystem and some contributions.

%description -l pl
U¿ytki dla podsystemu ISDN j±dra.

%prep
%setup -q
%patch -P 0 -p1
cp -p $RPM_SOURCE_DIR/isdn4k-utils-%{Version}.config .config

%build
make OPTIM="$RPM_OPT_FLAGS" oldconfig
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
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
