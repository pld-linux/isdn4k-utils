Summary:	Utilities for the kernel ISDN-subsystem
Summary(pl.UTF-8):	Narzędzia dla podsystemu ISDN jądra
Summary(pt_BR.UTF-8):	Utilitários para configuração do subsistema ISDN
Name:		isdn4k-utils
Version:	040111
Release:	4
Epoch:		2
License:	GPL v2
Group:		Applications/Communications
Source0:	http://rk.pop.e-wro.pl/%{name}-%{version}.tar.gz
# Source0-md5:	6955ecdcd7df5bc8fa2844fa9c45bbf6
Source1:	%{name}.config
Patch0:		%{name}-make.patch
Patch1:		%{name}-ppc.patch
Patch2:		%{name}-pppdcapiplugin.patch
Patch3:		%{name}-isdnlog_dont_touch_etc_services.patch
Patch4:		%{name}-libdir.patch
Patch5:		%{name}-am.patch
Patch6:		%{name}-libc.patch
Patch7:		%{name}-gcc.patch
Patch8:		%{name}-tcl.patch
Patch9:		%{name}-sh.patch
Patch10:	%{name}-opt.patch
URL:		http://www.isdn4linux.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-ext-devel
BuildRequires:	ppp-plugin-devel
BuildRequires:	rpmbuild(macros) >= 1.145
BuildRequires:	sed >= 4.0
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	xorg-cf-files >= 1.0.4-2
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-imake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin
%define		_appdefsdir	/usr/share/X11/app-defaults
%define		ppp_ver		%(awk -F'"' '/VERSION/ { print $2 }' /usr/include/pppd/patchlevel.h 2>/dev/null || echo ERROR)

%description
Utilities for the kernel ISDN-subsystem and some contributions.

%description -l pl.UTF-8
Narzędzia dla podsystemu ISDN jądra.

%description -l pt_BR.UTF-8
Utilitários para configuração do subsistema ISDN.

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
Requires:	xorg-data-bitmaps

%description devel
Developement files for isdn4k-tools.

%description devel -l pl.UTF-8
Pliki potrzebne do programowania z użyciem isdn4k-tools.

%package -n capi
Summary:	Program which can initialize CAPI hardware
Summary(pl.UTF-8):	Program inicjujący sprzęt ISDN zgodny z CAPI
Group:		Applications/Communications

%description -n capi
The Common ISDN Application Programming Interface - CAPI for short -
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains program which initialize your CAPI hardware. You
should install appropriate kernel module first and edit
/etc/capi.conf.

%description -n capi -l pl.UTF-8
Standard Common ISDN Application Programming Interface - w skrócie
CAPI - otwiera nowy wymiar w świecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezależny interfejs do sprzętu ISDN.

Ten pakiet zawiera program inicjalizujący kartę ISDN zgodną z CAPI.
Trzeba zaopatrzyć się w odpowiedni moduł jądra i zmodyfikować plik
/etc/capi.conf.

%package -n capi-libs
Summary:	CAPI 2.0 - shared library
Summary(pl.UTF-8):	Biblioteka dzielona CAPI 2.0
Group:		Libraries

%description -n capi-libs
The Common ISDN Application Programming Interface (CAPI for short)
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains shared library which provide CAPI 2.0.

%description -n capi-libs -l pl.UTF-8
Standard Common ISDN Application Programming Interface (w skrócie
CAPI) otwiera nowy wymiar w świecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezależny interfejs do sprzętu ISDN.

Ten pakiet zawiera bibliotekę dzieloną, która realizuje standard CAPI
w wersji 2.0.

%package -n capi-libs-static
Summary:	Static libraries for CAPI 2.0
Summary(pl.UTF-8):	Statyczne biblioteki dla CAPI 2.0
Group:		Development/Libraries
Requires:	capi-devel = %{epoch}:%{version}-%{release}

%description -n capi-libs-static
The Common ISDN Application Programming Interface (CAPI for short)
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains static library which provide CAPI 2.0.

%description -n capi-libs-static -l pl.UTF-8
Standard Common ISDN Application Programming Interface (w skrócie
CAPI) otwiera nowy wymiar w świecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezależny interfejs do sprzętu ISDN.

Ten pakiet zawiera bibliotekę statyczną, która realizuje standard CAPI
w wersji 2.0.

%package -n capi-devel
Summary:	CAPI 2.0 - development stuff
Summary(pl.UTF-8):	CAPI 2.0 - zasoby programistyczne
Group:		Development/Libraries
Requires:	capi-libs = %{epoch}:%{version}-%{release}

%description -n capi-devel
The Common ISDN Application Programming Interface (CAPI for short)
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains developement files for CAPI 2.0.

%description -n capi-devel -l pl.UTF-8
Standard Common ISDN Application Programming Interface (w skrócie
CAPI) otwiera nowy wymiar w świecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezależny interfejs do sprzętu ISDN.

Ten pakiet zawiera pliki niezbędne przy tworzeniu programów
wykorzystujących standard CAPI 2.0.

%package -n capi-tools
Summary:	CAPI 2.0 - useful programs
Summary(pl.UTF-8):	CAPI 2.0 - programy użytkowe
Group:		Applications/Communications

%description -n capi-tools
The Common ISDN Application Programming Interface (CAPI for short)
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains programs which can make use of your CAPI
compliant ISDN hardware.

%description -n capi-tools -l pl.UTF-8
Standard Common ISDN Application Programming Interface (w skrócie
CAPI) otwiera nowy wymiar w świecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezależny interfejs do sprzętu ISDN.

Ten pakiet zawiera programy, które potrafią zrobić użytek ze zgodnego
z CAPI sprzętu ISDN.

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
find . -type d -name CVS | xargs %{__rm} -r
%patch0 -p1
%ifarch ppc
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

# don't symlink app-defaults dir to /etc/X11
%{__sed} -i -e 's,@xmkmf,imake -I%{_libdir}/X11/config -DUseInstalled -DUseSeparateConfDir=NO,' xisdnload/Makefile.in

%build
cd capi20
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd ..
for i in capifax capiinfo capiinit rcapid; do
	cd $i
	%{__aclocal}
	%{__autoconf}
	%{__automake}
	cd ..
done
cd vbox
%{__aclocal}
%{__autoconf}
cd ..

cp %{SOURCE1} .config
%{__make} subconfig \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses" \
	CONFIG_LIBDIR=%{_libdir} \
	OPTIM="%{rpmcflags}"

# explicit CC/CCFLAGS for imontty and few other dirs
%{__make} \
	CC="%{__cc}" \
	CCFLAGS="%{rpmcflags}" \
	PPPVERSION=%{ppp_ver} \
	XAPPLOADDIR=%{_appdefsdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/var/lock/isdn}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	CONFIG_LIBDIR=%{_libdir} \
	INCROOT=%{_includedir} \
	PPPVERSION=%{ppp_ver} \
	XAPPLOADDIR=%{_appdefsdir}

test ! -d isdn-doc || %{__rm} -r isdn-doc
install -d isdn-doc/faq
%{__mv} $RPM_BUILD_ROOT%{_docdir}/isdn4linux/faq/*.{txt,html} isdn-doc/faq
%{__rm} $RPM_BUILD_ROOT%{_docdir}/isdn4linux/faq/*.sgml

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n capi-libs -p /sbin/ldconfig
%postun	-n capi-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README FAQ NEWS LEGAL.ipppcomp ipppcomp/README.LZS Mini-FAQ/isdn-faq.txt isdnlog/{tools/dest/README.*,isdnrep/CHANGES.isdnrep} FAQ/{_howto,_example} isdn-doc/faq
%dir %{_sysconfdir}/isdn
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/callerid.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/isdn.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/isdnlog.isdnctrl0.options
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/isdnlog.users
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/rate.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/vboxd.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/vboxgetty.conf
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/stop
%attr(755,root,root) %{_bindir}/autovbox
%attr(755,root,root) %{_bindir}/rmdtovbox
%attr(755,root,root) %{_bindir}/isdnbill
%attr(755,root,root) %{_bindir}/isdnconf
%attr(755,root,root) %{_bindir}/isdnrate
%attr(755,root,root) %{_bindir}/isdnrep
%attr(755,root,root) %{_bindir}/vbox
%attr(755,root,root) %{_bindir}/vboxbeep
%attr(755,root,root) %{_bindir}/vboxcnvt
%attr(755,root,root) %{_bindir}/vboxctrl
%attr(755,root,root) %{_bindir}/vboxmail
%attr(755,root,root) %{_bindir}/vboxmode
%attr(755,root,root) %{_bindir}/vboxplay
%attr(755,root,root) %{_bindir}/vboxtoau
%attr(755,root,root) %{_sbindir}/hisaxctrl
%attr(755,root,root) %{_sbindir}/icnctrl
%attr(755,root,root) %{_sbindir}/imon
%attr(755,root,root) %{_sbindir}/imontty
%attr(755,root,root) %{_sbindir}/ipppd
%attr(755,root,root) %{_sbindir}/ipppstats
%attr(755,root,root) %{_sbindir}/iprofd
%attr(755,root,root) %{_sbindir}/isdnctrl
%attr(755,root,root) %{_sbindir}/isdnlog
%attr(755,root,root) %{_sbindir}/loopctrl
%attr(755,root,root) %{_sbindir}/mkzonedb
%attr(755,root,root) %{_sbindir}/pcbitctl
%attr(755,root,root) %{_sbindir}/vboxd
%attr(755,root,root) %{_sbindir}/vboxgetty
%attr(755,root,root) %{_sbindir}/vboxputty
%{_prefix}/lib/isdn
%dir /var/lock/isdn
%{_mandir}/man1/autovbox.1*
%{_mandir}/man1/rmdtovbox.1*
%{_mandir}/man1/isdnconf.1*
%{_mandir}/man1/isdnrate.1*
%{_mandir}/man1/isdnrep.1*
%{_mandir}/man1/vbox.1*
%{_mandir}/man1/vboxbeep.1*
%{_mandir}/man1/vboxconvert.1*
%{_mandir}/man1/vboxctrl.1*
%{_mandir}/man1/vboxmode.1*
%{_mandir}/man1/vboxplay.1*
%{_mandir}/man1/vboxtoau.1*
%{_mandir}/man4/isdn_audio.4*
%{_mandir}/man4/isdnctrl.4*
%{_mandir}/man4/isdninfo.4*
%{_mandir}/man4/ttyI.4*
%{_mandir}/man5/callerid.conf.5*
%{_mandir}/man5/isdn.conf.5*
%{_mandir}/man5/isdnformat.5*
%{_mandir}/man5/isdnlog.5*
%{_mandir}/man5/isdnlog.users.5*
%{_mandir}/man5/rate-files.5*
%{_mandir}/man5/vbox.conf.5*
%{_mandir}/man5/vbox_file.5*
%{_mandir}/man5/vboxd.conf.5*
%{_mandir}/man5/vboxgetty.conf.5*
%{_mandir}/man5/vboxrc.5*
%{_mandir}/man5/vboxtcl.5*
%{_mandir}/man7/isdn_cause.7*
%{_mandir}/man8/.isdnctrl_conf.8*
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
%{_mandir}/man8/pcbitctl.8*
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

%files -n capi
%defattr(644,root,root,755)
%doc capiinit/capi.conf
%attr(755,root,root) %{_sbindir}/capiinit

%files -n capi-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcapi20.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcapi20.so.2

%files -n capi-libs-static
%defattr(644,root,root,755)
%{_libdir}/libcapi20.a
%{_libdir}/libcapi20dyn.a

%files -n capi-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcapi20.so
%{_libdir}/libcapi20.la
%{_includedir}/capi20.h
%{_includedir}/capicmd.h
%{_includedir}/capiutils.h

%files -n capi-tools
%defattr(644,root,root,755)
%doc rcapid/README
%attr(755,root,root) %{_sbindir}/avmcapictrl
%attr(755,root,root) %{_sbindir}/rcapid
%attr(755,root,root) %{_bindir}/capiinfo
%attr(755,root,root) %{_bindir}/capifax
%attr(755,root,root) %{_bindir}/capifaxrcvd
%{_mandir}/man8/avmcapictrl.8*
%{_mandir}/man8/capiinfo.8*

%files -n ppp-plugin-capi
%defattr(644,root,root,755)
%doc pppdcapiplugin/{README,examples/*,peers/*}
%attr(755,root,root) %{_libdir}/pppd/%{ppp_ver}/capiplugin.so
%attr(755,root,root) %{_libdir}/pppd/%{ppp_ver}/userpass.so
%{_mandir}/man8/capiplugin.8*
