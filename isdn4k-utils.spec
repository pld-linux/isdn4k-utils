Summary:	Utilities for the kernel ISDN-subsystem
Summary(pl):	U¿ytki dla podsystemu ISDN j±dra
Name:		isdn4k-utils
Version:	2.1b1
Release:	6
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Copyright:	distributable
Source0:	ftp://ftp.franken.de/pub/isdn4linux/v2.1/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}.config
Patch0:		%{name}-%{version}-COL.patch
URL:		http://www.franken.de/ftp/pub/isdn4linux/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Utilities for the kernel ISDN-subsystem and some contributions.

%description -l pl
U¿ytki dla podsystemu ISDN j±dra.

%prep
%setup -q
%patch -P 0 -p1
cp -p %{SOURCE1} .config

%build
%{__make} OPTIM="%{rpmcflags}" oldconfig
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} devices

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/isdn,%{_sbindir},%{_bindir},/var/lock/isdn} \
$RPM_BUILD_ROOT{/usr/X11R6/lib/X11/app-defaults,/usr/doc/faq/isdn4linux}

%{__make} install

cp -a $RPM_BUILD_ROOT/usr/doc/faq/isdn4linux ./isdn4linux-faq

install isdnlog/isdnrep/isdnrep.1 $RPM_BUILD_ROOT%{_mandir}/man1
install isdnlog/isdnlog/isdnlog.8 $RPM_BUILD_ROOT%{_mandir}/man8
echo ".so ttyI.4" > $RPM_BUILD_ROOT%{_mandir}/man4/cui.4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README isdn4linux-faq
%dir /var/lock/isdn

%dir %{_sysconfdir}/isdn
%config %{_sysconfdir}/isdn/callerid.conf
%config %{_sysconfdir}/isdn/isdn.conf

/dev/*

%attr(755,root,root) %{_sbindir}/avmcapictrl
%attr(755,root,root) %{_sbindir}/hisaxctrl
%attr(755,root,root) %{_sbindir}/icnctrl
%attr(755,root,root) %{_sbindir}/imon
%attr(755,root,root) %{_sbindir}/imontty
%attr(755,root,root) %{_sbindir}/ipppd
%attr(755,root,root) %{_sbindir}/ipppstats
%attr(755,root,root) %{_sbindir}/iprofd
%attr(755,root,root) %{_sbindir}/isdnctrl
%attr(755,root,root) %{_sbindir}/isdnlog
%attr(755,root,root) %{_sbindir}/pcbitctl
%attr(755,root,root) %{_sbindir}/telesctrl

/usr/X11R6/lib/X11/app-defaults/XISDNLoad

%attr(755,root,root) %{_bindir}/isdnconf
%attr(755,root,root) %{_bindir}/isdnrep
%attr(755,root,root) %{_bindir}/xisdnload
%attr(755,root,root) %{_bindir}/xmonisdn

%dir %{_libdir}/isdn
%{_libdir}/isdn/areacodes

%{_libdir}/vbox

%{_mandir}/man1/isdnrep.1*
%{_mandir}/man1/xisdnload.1x*
%{_mandir}/man1/xmonisdn.1x*
%{_mandir}/man4/cui.4*
%{_mandir}/man4/ttyI.4*
%{_mandir}/man4/isdninfo.4*
%{_mandir}/man4/isdn_audio.4*
%{_mandir}/man7/isdn_cause.7*
%{_mandir}/man8/avmcapictrl.8*
%{_mandir}/man8/hisaxctrl.8*
%{_mandir}/man8/icnctrl.8*
%{_mandir}/man8/imon.8*
%{_mandir}/man8/ipppd.8*
%{_mandir}/man8/ipppstats.8*
%{_mandir}/man8/iprofd.8*
%{_mandir}/man8/isdnctrl.8*
%{_mandir}/man8/telesctrl.8*
