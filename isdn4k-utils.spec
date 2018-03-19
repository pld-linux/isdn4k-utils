Summary:	Utilities for the kernel ISDN-subsystem
Summary(pl.UTF-8):	Narzędzia dla podsystemu ISDN jądra
Summary(pt_BR.UTF-8):	Utilitários para configuração do subsistema ISDN
Name:		isdn4k-utils
Version:	3.27
Release:	3
Epoch:		3
License:	GPL v2
Group:		Applications/Communications
# git clone git://git.misdn.eu/isdn4k-utils.git
# git checkout v3.25
Source0:	%{name}-%{version}.tar.xz
# Source0-md5:	09d3d6fbb3e1f69776e7a9ada836e074
Source1:	%{name}.config
Source2:	capi.conf
Source3:	capi.init
Patch0:		%{name}-make.patch
Patch1:		%{name}-pppdcapiplugin.patch
Patch2:		%{name}-am.patch
Patch3:		%{name}-sh.patch
Patch4:		%{name}-opt.patch
Patch5:		%{name}-link.patch
Patch6:		%{name}-rcapid.patch
Patch7:		use-va_copy.patch
Patch8:		format-security.patch
Patch9:		tcl8.6.patch
Patch10:	gnu89-inline.patch
Patch11:	perl-wld-module.patch
URL:		http://www.isdn4linux.de/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-ext-devel
BuildRequires:	ppp-plugin-devel
BuildRequires:	rpmbuild(macros) >= 1.145
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	xorg-cf-files >= 1.0.4-2
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-imake
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/share/X11/app-defaults
%define		ppp_ver		%(awk -F'"' '/VERSION/ { print $2 }' /usr/include/pppd/patchlevel.h 2>/dev/null || echo ERROR)

%description
Utilities for the kernel ISDN-subsystem and some contributions.

%description -l pl.UTF-8
Narzędzia dla podsystemu ISDN jądra.

%description -l pt_BR.UTF-8
Utilitários para configuração do subsistema ISDN.

%package vbox
Summary:	VBOX - Voice Answering Machine for isdn4linux
Summary(pl.UTF-8):	VBOX - automatyczna sekretarka dla szkieletu isdn4linux
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description vbox
VBOX - Voice Answering Machine for isdn4linux.

%description vbox -l pl.UTF-8
VBOX - automatyczna sekretarka dla szkieletu isdn4linux.

%package x11
Summary:	Utilities for the kernel ISDN-subsystem - frontend for X11
Summary(pl.UTF-8):	Narzędzia dla podsystemu ISDN jądra - nakladki dla X11
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	xorg-lib-libXt >= 1.0.0

%description x11
Utilities for the kernel ISDN-subsystem and some contributions (X11).

%description x11 -l pl.UTF-8
Narzędzia dla podsystemu ISDN jądra, nakładki graficzne (X11).

# rename to -x11-bitmaps ?
%package devel
Summary:	Developement files for isdn4k-tools
Summary(pl.UTF-8):	Pliki potrzebne do programowania z użyciem isdn4k-tools
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	xorg-data-xbitmaps

%description devel
Developement files for isdn4k-tools.

%description devel -l pl.UTF-8
Pliki potrzebne do programowania z użyciem isdn4k-tools.

%package -n capi4k-utils
Summary:	Configuration tools for CAPI hardware
Summary(pl.UTF-8):	Programy konfiguracyjne do sprzętu CAPI
Group:		Applications/Communications
Requires:	capi4k-utils-libs = %{epoch}:%{version}-%{release}
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
Obsoletes:	capi
Obsoletes:	capi-tools
Obsoletes:	capi4k-utils-remotecapi

%description -n capi4k-utils
The Common ISDN Application Programming Interface - CAPI for short -
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains programs which initialize your CAPI hardware.
You should install appropriate kernel module first and edit
/etc/capi.conf.

%description -n capi4k-utils -l pl.UTF-8
Standard Common ISDN Application Programming Interface - w skrócie
CAPI - otwiera nowy wymiar w świecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezależny interfejs do sprzętu ISDN.

Ten pakiet zawiera programy inicjalizujące karty ISDN zgodne z CAPI.
Trzeba zaopatrzyć się w odpowiedni moduł jądra i zmodyfikować plik
/etc/capi.conf.

%package -n capi4k-utils-capifax
Summary:	CAPI 2.0 fax tool
Summary(de.UTF-8):	CAPI 2.0 Fax Programm
Summary(pl.UTF-8):	Proste narzędzie do faksowania z użyciem CAPI 2.0
Group:		Applications/Communications
Requires:	capi4k-utils = %{epoch}:%{version}-%{release}

%description -n capi4k-utils-capifax
The Common ISDN Application Programming Interface (CAPI for short)
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains native tools for sending and receiving fax with
CAPI 2.0.

%description -n capi4k-utils-capifax -l pl.UTF-8
Standard Common ISDN Application Programming Interface (w skrócie
CAPI) otwiera nowy wymiar w świecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezależny interfejs do sprzętu ISDN.

Ten pakiet zawiera natywne narzędzia do wysyłania i odbierania faksów
przy użyciu CAPI 2.0.

%package -n capi4k-utils-libs
Summary:	CAPI 2.0 - shared library
Summary(pl.UTF-8):	Biblioteka dzielona CAPI 2.0
Group:		Libraries
Obsoletes:	capi-libs
Conflicts:	capi4k-utils < 3:3.25

%description -n capi4k-utils-libs
The Common ISDN Application Programming Interface (CAPI for short)
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains shared library which provides CAPI 2.0.

%description -n capi4k-utils-libs -l pl.UTF-8
Standard Common ISDN Application Programming Interface (w skrócie
CAPI) otwiera nowy wymiar w świecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezależny interfejs do sprzętu ISDN.

Ten pakiet zawiera bibliotekę dzieloną, która realizuje standard CAPI
w wersji 2.0.

%package -n capi4k-utils-devel
Summary:	CAPI 2.0 - development files
Summary(pl.UTF-8):	CAPI 2.0 - pliki programistyczne
Group:		Development/Libraries
Requires:	capi4k-utils-libs = %{epoch}:%{version}-%{release}
Obsoletes:	capi-devel

%description -n capi4k-utils-devel
The Common ISDN Application Programming Interface (CAPI for short)
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains developement files for CAPI 2.0.

%description -n capi4k-utils-devel -l pl.UTF-8
Standard Common ISDN Application Programming Interface (w skrócie
CAPI) otwiera nowy wymiar w świecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezależny interfejs do sprzętu ISDN.

Ten pakiet zawiera pliki niezbędne przy tworzeniu programów
wykorzystujących standard CAPI 2.0.

%package -n capi4k-utils-static
Summary:	Static libraries for CAPI 2.0
Summary(pl.UTF-8):	Statyczne biblioteki dla CAPI 2.0
Group:		Development/Libraries
Requires:	capi4k-utils-devel = %{epoch}:%{version}-%{release}
Obsoletes:	capi-libs-static

%description -n capi4k-utils-static
The Common ISDN Application Programming Interface (CAPI for short)
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains static library which provide CAPI 2.0.

%description -n capi4k-utils-static -l pl.UTF-8
Standard Common ISDN Application Programming Interface (w skrócie
CAPI) otwiera nowy wymiar w świecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezależny interfejs do sprzętu ISDN.

Ten pakiet zawiera bibliotekę statyczną, która realizuje standard CAPI
w wersji 2.0.

%package -n ppp-plugin-capi
Summary:	CAPI plugin for pppd-%{ppp_ver}
Summary(pl.UTF-8):	Wtyczka CAPI dla pppd w wersji %{ppp_ver}
Group:		Applications/Communications
%{requires_eq_to ppp ppp-plugin-devel}

%description -n ppp-plugin-capi
CAPI plugin for pppd-%{ppp_ver}.

%description -n ppp-plugin-capi -l pl.UTF-8
Wtyczka CAPI dla pppd w wersji %{ppp_ver}.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

# don't symlink app-defaults dir to /etc/X11
%{__sed} -i -e 's,@xmkmf,imake -I%{_libdir}/X11/config -DUseInstalled -DUseSeparateConfDir=NO,' xisdnload/Makefile.in

%build
cd capi20
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd ..
for i in capifax capiinfo capiinit rcapid vbox; do
	cd $i
	%{__aclocal}
	%{__autoconf}
	[ "$i" == "rcapid" ] || %{__autoheader}
	%{__automake}
	cd ..
done

cp %{SOURCE1} .config
%{__make} -j1 subconfig \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses" \
	CONFIG_LIBDIR=%{_libdir} \
	OPTIM="%{rpmcflags}"

# explicit CC/CCFLAGS for imontty and few other dirs
%{__make} -j1 \
	CC="%{__cc}" \
	CCFLAGS="%{rpmcflags}" \
	PPPVERSION=%{ppp_ver} \
	XAPPLOADDIR=%{_appdefsdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/var/lock/isdn,/sbin}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	CONFIG_LIBDIR=%{_libdir} \
	INCROOT=%{_includedir} \
	PPPVERSION=%{ppp_ver} \
	XAPPLOADDIR=%{_appdefsdir}

install -D %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/capi.conf
install -D %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/capi

# Firmware goes here - see LSB and kernel 2.6.x ISDN stuff
install -d $RPM_BUILD_ROOT%{_datadir}/isdn

test ! -d isdn-doc || %{__rm} -r isdn-doc
install -d isdn-doc/faq
%{__mv} $RPM_BUILD_ROOT%{_docdir}/isdn4linux/faq/*.{txt,html} isdn-doc/faq
%{__rm} $RPM_BUILD_ROOT%{_docdir}/isdn4linux/faq/*.sgml

# vbox.txt packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/vbox

%{__rm} $RPM_BUILD_ROOT%{_libdir}/capi/lib_capi_mod_*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -n capi4k-utils
/sbin/chkconfig --add capi
%service capi restart

%preun -n capi4k-utils
if [ "$1" = "0" ]; then
	%service capi stop
	/sbin/chkconfig --del capi
fi

%post	-n capi4k-utils-libs -p /sbin/ldconfig
%postun	-n capi4k-utils-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README FAQ NEWS LEGAL.ipppcomp ipppcomp/README.LZS Mini-FAQ/isdn-faq.txt isdnlog/{tools/dest/README.*,isdnrep/CHANGES.isdnrep} FAQ/{_howto,_example} isdn-doc/faq
%dir %{_sysconfdir}/isdn
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/callerid.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/isdn.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/isdnlog.isdnctrl0.options
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/isdnlog.users
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/rate.conf
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/stop
%attr(755,root,root) %{_bindir}/isdnbill
%attr(755,root,root) %{_bindir}/isdnconf
%attr(755,root,root) %{_bindir}/isdnrate
%attr(755,root,root) %{_bindir}/isdnrep
%attr(755,root,root) /sbin/actctrl
%attr(755,root,root) /sbin/hisaxctrl
%attr(755,root,root) /sbin/icnctrl
%attr(755,root,root) /sbin/imon
%attr(755,root,root) /sbin/imontty
%attr(755,root,root) /sbin/ipppd
%attr(755,root,root) /sbin/ipppstats
%attr(755,root,root) /sbin/iprofd
%attr(755,root,root) /sbin/isdnctrl
%attr(755,root,root) /sbin/isdnlog
%attr(755,root,root) /sbin/loopctrl
%attr(755,root,root) /sbin/mkzonedb
%{_prefix}/lib/isdn
%dir /var/lock/isdn
%{_mandir}/man1/isdnbill.1*
%{_mandir}/man1/isdnconf.1*
%{_mandir}/man1/isdnrate.1*
%{_mandir}/man1/isdnrep.1*
%{_mandir}/man4/isdn_audio.4*
%{_mandir}/man4/isdnctrl.4*
%{_mandir}/man4/isdninfo.4*
%{_mandir}/man4/ttyI.4*
%{_mandir}/man5/callerid.conf.5*
%{_mandir}/man5/isdn.conf.5*
%{_mandir}/man5/isdnformat.5*
%{_mandir}/man5/isdnlog.5*
%{_mandir}/man5/isdnlog.users.5*
%{_mandir}/man5/rate.conf.5*
%{_mandir}/man5/rate-files.5*
%{_mandir}/man7/isdn_cause.7*
%{_mandir}/man8/.isdnctrl_conf.8*
%{_mandir}/man8/actctrl.8*
%{_mandir}/man8/hisaxctrl.8*
%{_mandir}/man8/icnctrl.8*
%{_mandir}/man8/imon.8*
%{_mandir}/man8/imontty.8*
%{_mandir}/man8/ipppd.8*
%{_mandir}/man8/ipppstats.8*
%{_mandir}/man8/iprofd.8*
%{_mandir}/man8/isdnctrl.8*
%{_mandir}/man8/isdnlog.8*
%{_mandir}/man8/loopctrl.8*
%{_mandir}/man8/mkzonedb.8*

%files vbox
%defattr(644,root,root,755)
%doc vbox/{CHANGES,README} vbox/doc/de/vbox.txt
%attr(755,root,root) %{_bindir}/autovbox
%attr(755,root,root) %{_bindir}/rmdtovbox
%attr(755,root,root) %{_bindir}/vbox
%attr(755,root,root) %{_bindir}/vboxbeep
%attr(755,root,root) %{_bindir}/vboxcnvt
%attr(755,root,root) %{_bindir}/vboxctrl
%attr(755,root,root) %{_bindir}/vboxmode
%attr(755,root,root) %{_bindir}/vboxplay
%attr(755,root,root) %{_bindir}/vboxtoau
%attr(755,root,root) %{_sbindir}/vboxd
%attr(755,root,root) %{_sbindir}/vboxgetty
%attr(755,root,root) %{_sbindir}/vboxmail
%attr(755,root,root) %{_sbindir}/vboxputty
%dir %{_sysconfdir}/vbox
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vbox/vboxd.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vbox/vboxgetty.conf
%{_mandir}/man1/autovbox.1*
%{_mandir}/man1/rmdtovbox.1*
%{_mandir}/man1/vbox.1*
%{_mandir}/man1/vboxbeep.1*
%{_mandir}/man1/vboxconvert.1*
%{_mandir}/man1/vboxctrl.1*
%{_mandir}/man1/vboxmode.1*
%{_mandir}/man1/vboxplay.1*
%{_mandir}/man1/vboxtoau.1*
%{_mandir}/man5/vbox.conf.5*
%{_mandir}/man5/vbox_file.5*
%{_mandir}/man5/vboxd.conf.5*
%{_mandir}/man5/vboxgetty.conf.5*
%{_mandir}/man5/vboxrc.5*
%{_mandir}/man5/vboxtcl.5*
%{_mandir}/man8/vboxd.8*
%{_mandir}/man8/vboxgetty.8*
%{_mandir}/man8/vboxmail.8*
%{_mandir}/man8/vboxputty.8*

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xisdnload
%attr(755,root,root) %{_bindir}/xmonisdn
%{_appdefsdir}/XISDNLoad
%{_mandir}/man1/xisdnload.1x*
%{_mandir}/man1/xmonisdn.1x*

%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/bitmaps/net*

%files -n capi4k-utils
%defattr(644,root,root,755)
%doc rcapid/README capiinit/capi.conf
%attr(755,root,root) /sbin/avmcapictrl
%attr(755,root,root) /sbin/capiinit
%attr(755,root,root) /sbin/rcapid
%attr(755,root,root) %{_bindir}/capiinfo
%dir %{_datadir}/isdn
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/capi.conf
%attr(754,root,root) /etc/rc.d/init.d/capi
%{_mandir}/man8/avmcapictrl.8*
%{_mandir}/man8/capiinfo.8*
%{_mandir}/man8/capiinit.8*
%{_mandir}/man8/rcapid.8*

%files -n capi4k-utils-capifax
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/capifax
%attr(755,root,root) %{_bindir}/capifaxrcvd
%{_mandir}/man1/capifax.1*
%{_mandir}/man8/capifaxrcvd.8*

%files -n capi4k-utils-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcapi20.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcapi20.so.3
%dir %{_libdir}/capi
%attr(755,root,root) %{_libdir}/capi/lib_capi_mod_fritzbox.so*
%attr(755,root,root) %{_libdir}/capi/lib_capi_mod_rcapi.so*
%attr(755,root,root) %{_libdir}/capi/lib_capi_mod_std.so*

%files -n capi4k-utils-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcapi20.so
%{_libdir}/libcapi20.la
%{_includedir}/capi20.h
%{_includedir}/capi_debug.h
%{_includedir}/capi_mod.h
%{_includedir}/capicmd.h
%{_includedir}/capiutils.h
%{_pkgconfigdir}/capi20.pc

%files -n capi4k-utils-static
%defattr(644,root,root,755)
%{_libdir}/libcapi20.a
%{_libdir}/libcapi20dyn.a

%files -n ppp-plugin-capi
%defattr(644,root,root,755)
%doc pppdcapiplugin/{README,examples/*,peers/*}
%attr(755,root,root) %{_libdir}/pppd/plugins/capiplugin.so
%attr(755,root,root) %{_libdir}/pppd/plugins/userpass.so
%{_mandir}/man8/capiplugin.8*
