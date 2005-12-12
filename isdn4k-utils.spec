Summary:	Utilities for the kernel ISDN-subsystem
Summary(pl):	Narzêdzia dla podsystemu ISDN j±dra
Summary(pt_BR):	Utilitários para configuração do subsistema ISDN
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
URL:		http://www.isdn4linux.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-ext-devel
BuildRequires:	ppp-plugin-devel
BuildRequires:	rpmbuild(macros) >= 1.145
BuildRequires:	tcl-devel >= 8.3.4-10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin
%define		xincludedir	/usr/X11R6/include/X11
%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults
%define		ppp_ver		%(awk -F'"' '/VERSION/ { print $2 }' /usr/include/pppd/patchlevel.h 2>/dev/null || echo ERROR)

%description
Utilities for the kernel ISDN-subsystem and some contributions.

%description -l pl
Narzêdzia dla podsystemu ISDN j±dra.

%description -l pt_BR
Utilitários para configuração do subsistema ISDN.

%package x11
Summary:	Utilities for the kernel ISDN-subsystem - frontend for X11
Summary(pl):	Narzêdzia dla podsystemu ISDN j±dra - nakladki dla X11
Group:		Applications/Communications
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description x11
Utilities for the kernel ISDN-subsystem and some contributions (X11).

%description x11 -l pl
Narzêdzia dla podsystemu ISDN j±dra, nak³adki graficzne (X11).

%package devel
Summary:	Developement files for isdn4k-tools
Summary(pl):	Pliki potrzebne do programowania z u¿yciem isdn4k-tools
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Developement files for isdn4k-tools.

%description devel -l pl
Pliki potrzebne do programowania z u¿yciem isdn4k-tools.

%package -n ppp-plugin-capi
Summary:	capiplugin for pppd-%{ppp_ver}
Summary(pl):	Wtyczka capi dla pppd w wersji %{ppp_ver}
Group:		Applications/Communications
%{requires_eq_to ppp ppp-plugin-devel}

%description -n ppp-plugin-capi
capiplugin for pppd-%{ppp_ver}.

%description -n ppp-plugin-capi -l pl
Wtyczka capi dla pppd w wersji %{ppp_ver}.

%package -n capi
Summary:	Program which can initialize CAPI hardware
Summary(pl):	Program, który inicjalizuje sprzêt ISDN zgodny z CAPI
Group:		Applications/Communications

%description -n capi
The Common ISDN Application Programming Interface - CAPI for short -
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains program which initialize your CAPI hardware. You
should install appropriate kernel module first and edit
/etc/capi.conf.

%description -n capi -l pl
Standard Common ISDN Application Programming Interface - w skrócie
CAPI - otwiera nowy wymiar w ¶wiecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezale¿ny interfejs do sprzêtu ISDN.

Ten pakiet zawiera program inicjalizuj±cy kartê ISDN zgodn± z CAPI.
Trzeba zaopatrzyæ siê w odpowiedni modu³ j±dra i zmodyfikowaæ plik
/etc/capi.conf.

%package -n capi-libs
Summary:	CAPI 2.0 - shared library
Summary(pl):	Biblioteka dzielona CAPI 2.0
Group:		Libraries

%description -n capi-libs
The Common ISDN Application Programming Interface (CAPI for short)
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains shared library which provide CAPI 2.0.

%description -n capi-libs -l pl
Standard Common ISDN Application Programming Interface (w skrócie
CAPI) otwiera nowy wymiar w ¶wiecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezale¿ny interfejs do sprzêtu ISDN.

Ten pakiet zawiera bibliotekê dzielon±, która realizuje standard CAPI
w wersji 2.0.

%package -n capi-libs-static
Summary:	Static libraries for CAPI 2.0
Summary(pl):	Statyczne biblioteki dla CAPI 2.0
Group:		Development/Libraries
Requires:	capi-devel = %{epoch}:%{version}-%{release}

%description -n capi-libs-static
The Common ISDN Application Programming Interface (CAPI for short)
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains static library which provide CAPI 2.0.

%description -n capi-libs-static -l pl
Standard Common ISDN Application Programming Interface (w skrócie
CAPI) otwiera nowy wymiar w ¶wiecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezale¿ny interfejs do sprzêtu ISDN.

Ten pakiet zawiera bibliotekê statyczn±, która realizuje standard CAPI
w wersji 2.0.

%package -n capi-devel
Summary:	CAPI 2.0 - development stuff
Summary(pl):	CAPI 2.0 - zasoby programistyczne
Group:		Development/Libraries
Requires:	capi-libs = %{epoch}:%{version}-%{release}

%description -n capi-devel
The Common ISDN Application Programming Interface (CAPI for short)
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains developement files for CAPI 2.0.

%description -n capi-devel -l pl
Standard Common ISDN Application Programming Interface (w skrócie
CAPI) otwiera nowy wymiar w ¶wiecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezale¿ny interfejs do sprzêtu ISDN.

Ten pakiet zawiera pliki niezbêdne przy tworzeniu programów
wykorzystuj±cych standard CAPI 2.0

%package -n capi-tools
Summary:	CAPI 2.0 - useful programs
Summary(pl):	CAPI 2.0 - programy u¿ytkowe
Group:		Applications/Communications

%description -n capi-tools
The Common ISDN Application Programming Interface (CAPI for short)
opens up a new dimension in communication technologies. It provides a
uniform, independent interface to ISDN hardware components.

This package contains programs which can make use of your CAPI
compilant ISDN hardware

%description -n capi-tools -l pl
Standard Common ISDN Application Programming Interface (w skrócie
CAPI) otwiera nowy wymiar w ¶wiecie technologii komunikacyjnych.
Dostarcza ujednolicony, niezale¿ny interfejs do sprzêtu ISDN.

Ten pakiet zawiera programy, które potrafi± zrobiæ u¿ytek ze zgodnego
z CAPI sprzêtu ISDN.

%prep
%setup -q -n %{name}
%patch0 -p1
%ifarch ppc
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
for i in capi20 capifax capiinfo capiinit rcapid; do
	cd $i
	%{__libtoolize}
	%{__aclocal}
	%{__autoconf}
	%{__automake}
	cd ..
done

cp %{SOURCE1} .config
%{__make} subconfig \
	CONFIG_LIBDIR=%{_libdir} \
	OPTIM="%{rpmcflags}"\
	CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"

%{__make} \
	PPPVERSION=%{ppp_ver} \
	CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/var/lock/isdn,%{_datadir}/doc/%{name}-%{version}/faq}

%{__make} install \
	PPPVERSION=%{ppp_ver} \
	CONFIG_LIBDIR=%{_libdir} \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/doc/isdn4linux/faq/*.txt \
	$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/faq
mv -f $RPM_BUILD_ROOT%{_datadir}/doc/isdn4linux/faq/*.html \
	$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/faq
mv -f $RPM_BUILD_ROOT%{_datadir}/doc/vbox/*.txt \
	$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n capi-libs -p /sbin/ldconfig
%postun	-n capi-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README FAQ NEWS LEGAL.ipppcomp ipppcomp/README.LZS Mini-FAQ/*.txt
%doc isdnlog/{tools/dest/README*,isdnrep/CHANGES*}
%doc FAQ/{_howto,_example}
%dir %{_sysconfdir}/isdn
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/isdn/*
%attr(755,root,root) %{_bindir}/[!cx]*
%attr(755,root,root) %{_sbindir}/[!acr]*
%{_prefix}/lib/isdn
%dir /var/lock/isdn
%{_mandir}/man1/[!x]*
%{_mandir}/man[457]/*
%{_mandir}/man8/[!ac]*
%{_mandir}/man8/.isdnctrl_conf.8*

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xisdnload
%attr(755,root,root) %{_bindir}/xmonisdn
%{_appdefsdir}/XISDNLoad
%{_mandir}/man1/xisdnload.1x*
%{_mandir}/man1/xmonisdn.1x*

%files devel
%defattr(644,root,root,755)
%{xincludedir}/bitmaps/*

%files -n capi-libs-static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files -n ppp-plugin-capi
%defattr(644,root,root,755)
%doc pppdcapiplugin/{README,examples/*,peers/*}
%attr(755,root,root) %{_libdir}/pppd/%{ppp_ver}/*
%{_mandir}/man8/capiplugin*

%files -n capi-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files -n capi-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*.h

%files -n capi-tools
%defattr(644,root,root,755)
%doc rcapid/README
%attr(755,root,root) %{_sbindir}/[ar]*
%attr(755,root,root) %{_bindir}/capiinfo
%attr(755,root,root) %{_bindir}/capifax*
%{_mandir}/man8/avmcapi*
%{_mandir}/man8/capiinfo*

%files -n capi
%defattr(644,root,root,755)
%doc capiinit/capi.conf
%attr(755,root,root) %{_sbindir}/capiinit
