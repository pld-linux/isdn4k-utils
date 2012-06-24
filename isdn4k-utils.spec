Summary:	Utilities for the kernel ISDN-subsystem
Summary(pl):	U�ytki dla podsystemu ISDN j�dra
Summary(pt_BR):	Utilit�rios para configura��o do subsistema ISDN
Name:		isdn4k-utils
Version:	0208190200
Release:	4
License:	GPL v2
Group:		Applications/Communications
Source0:	ftp://ftp.suse.com/pub/isdn4linux/v2.1/isdn4k-utils/%{name}-%{version}.tar.gz
Source1:        %{name}.config
Patch0:		%{name}-make.patch
Patch1:		%{name}-ppc.patch
Patch2:		%{name}-pppdcapiplugin.patch
URL:		http://www.isdn4linux.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin
%define		_xprefix	/usr/X11R6
%define		_xbindir	%{_xprefix}/bin
%define		_xincludedir	%{_xprefix}/include
%define		_xlibdir	%{_xprefix}/lib
%define		_xmandir	%{_xprefix}/man

%description
Utilities for the kernel ISDN-subsystem and some contributions.

%description -l pl
Narz�dzia dla podsystemu ISDN j�dra.

%description -l pt_BR
Utilit�rios para configura��o do subsistema ISDN.

%package x11
Summary:        Utilities for the kernel ISDN-subsystem - frontend for X11
Summary(pl):    Narz�dzia dla podsystemu ISDN j�dra - nakladki dla X11
Group:          Applications/Communications
Requires:       %{name} = %{version}
%description x11
Utilities for the kernel ISDN-subsystem and some contributions (X11).

%description x11 -l pl
Narz�dzia dla podsystemu ISDN j�dra, nak�adki graficzne (X11).

%package devel
Summary:	Developement files for isdn4k-tools
Summary(pl):	Rzeczy potrzebne do programowania z u�yciem isdn4k-tools
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Developement files for isdn4k-tools.

%description devel -l pl
Rzeczy potrzebne do programowania z u�yciem isdn4k-tools.


%define		ppp_ver	2.4.1
%package -n ppp-capiplugin
Summary:	capiplugin for pppd-%{ppp_ver}
Summary(pl):	Wtyczka capi dla pppd w wersji %{ppp_ver}
Group:		Sieciowe/Serwery
Requires:	ppp = %{ppp_ver}

%description -n ppp-capiplugin
capiplugin for pppd-%{ppp_ver}

%description -n ppp-capiplugin -l pl
Wtyczka capi dla pppd w wersji %{ppp_ver}

%package -n capi
Summary:	Program which can initialize CAPI hardware 
Summary(pl):	Program, kt�ry inicjalizuje sprz�t ISDN zgodny z CAPI  
Group:		System/Administration

%description -n capi
The Common ISDN Application Programming Interface - CAPI for short
- opens up a new dimension in communication technologies. It provides
a uniform, independent interface to ISDN hardware components.

This package contains program which initialize your CAPI hardware.
You shoul install appropriate kernel module first and edit 
/etc/capi.conf.

%description -n capi -l pl
Standard Common ISDN Application Programming Interface - w skr�cie CAPI
- otwiera nowy wymiar w �wiecie technologi komunikacyjnych. Dostarcza
ujednolicony, niezale�ny interfejs do sprz�tu ISDN.

Ten pakiet zawiera program, kt�ry zainicjuje twoj� kart� ISDN zgodn� z CAPI
Powiniene� zaopatrzy� si� w odpowiedni modu� j�dra i wyedytowa� plik
/etc/capi.conf.

%package -n capi-libs
Summary:	CAPI 2.0 - shared library
Summary(pl):	biblioteka dzielona CAPI 2.0
Group:		Development/Libraries


%description -n capi-libs
The Common ISDN Application Programming Interface - CAPI for short 
- opens up a new dimension in communication technologies. It provides 
a uniform, independent interface to ISDN hardware components.

This package contains shared library which provide CAPI 2.0.

%description -n capi-libs -l pl
Standard Common ISDN Application Programming Interface - w skr�cie CAPI
- otwiera nowy wymiar w �wiecie technologi komunikacyjnych. Dostarcza
ujednolicony, niezale�ny interfejs do sprz�tu ISDN.

Ten pakiet zawiera bibliotek� dzielon�, kt�ra realizuje standard CAPI 
w wersji 2.0

%package -n capi-libs-static
Summary:	Static libraries for CAPI 2.0
Summary(pl):	Statyczne biblioteki dla CAPI 2.0
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description -n capi-libs-static
The Common ISDN Application Programming Interface - CAPI for short
- opens up a new dimension in communication technologies. It provides
a uniform, independent interface to ISDN hardware components.

This package contains static library which provide CAPI 2.0.


%description -n capi-libs-static -l pl
Standard Common ISDN Application Programming Interface - w skr�cie CAPI
- otwiera nowy wymiar w �wiecie technologi komunikacyjnych. Dostarcza
ujednolicony, niezale�ny interfejs do sprz�tu ISDN.

Ten pakiet zawiera bibliotek� statyczn�, kt�ra realizuje standard CAPI
w wersji 2.0

%package -n capi-devel
Summary:        CAPI 2.0 - development staff
Summary(pl):    CAPI 2.0 - narz�dzia dewelopera
Group:          Development/Libraries
Requires:       capi-libs = %{version}

%description -n capi-devel

The Common ISDN Application Programming Interface - CAPI for short
- opens up a new dimension in communication technologies. It provides
a uniform, independent interface to ISDN hardware components.

This package contains developement files for CAPI 2.0.


%description -n capi-devel -l pl
Standard Common ISDN Application Programming Interface - w skr�cie CAPI
- otwiera nowy wymiar w �wiecie technologi komunikacyjnych. Dostarcza
ujednolicony, niezale�ny interfejs do sprz�tu ISDN.

Ten pakiet zawiera pliki niezb�dne przy towrzeniu program�w wykorzystuj�cych
standard CAPI 2.0

%package -n capi-tools
Summary:        CAPI 2.0 - useful programs
Summary(pl):    CAPI 2.0 - programy u�ytkowe
Group:          Applications/Communications

%description -n capi-tools
The Common ISDN Application Programming Interface - CAPI for short
- opens up a new dimension in communication technologies. It provides
a uniform, independent interface to ISDN hardware components.

This package contains programs which can make use of your CAPI compilant
ISDN hardware

%description -n capi-tools -l pl
Standard Common ISDN Application Programming Interface - w skr�cie CAPI
- otwiera nowy wymiar w �wiecie technologi komunikacyjnych. Dostarcza
ujednolicony, niezale�ny interfejs do sprz�tu ISDN.

Ten pakiet zawiera programy, kt�re potrafi� zrobic u�ytek z twojego
zgodnego z CAPI sprz�tu ISDN.

%prep
%setup -q -n %{name}
%patch0 -p1
%ifarch ppc
%patch1 -p1
%endif
%patch2 -p1

%build
for i in capi20 capifax capiinfo capiinit rcapid; do
	cd $i
	rm -f missing
	%{__libtoolize}
	aclocal
	%{__autoconf}
	%{__automake}
	cd ..
done

cp %{SOURCE1} .config
%{__make} OPTIM="%{rpmcflags}" subconfig
%{__make} PPPVERSIONS=%{ppp_ver} CFLAGS="%{rpmcflags} -I/usr/include/ncurses/"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/var/lock/isdn,%{_datadir}/doc/%{name}-%{version}/faq,%{_xbindir}}

%{__make} PPPVERSIONS=%{ppp_ver} DESTDIR=$RPM_BUILD_ROOT install

mv $RPM_BUILD_ROOT%{_datadir}/doc/isdn4linux/faq/*.txt \
	$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/faq
mv $RPM_BUILD_ROOT%{_datadir}/doc/isdn4linux/faq/*.html \
	$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/faq
mv $RPM_BUILD_ROOT%{_datadir}/doc/vbox/*.txt \
	$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
mv $RPM_BUILD_ROOT%{_bindir}/{xisdnload,xmonisdn} \
	$RPM_BUILD_ROOT%{_xbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README FAQ NEWS LEGAL.ipppcomp ipppcomp/README.LZS Mini-FAQ/*.txt
%doc isdnlog/{tools/dest/README*,isdnrep/CHANGES*}
%doc FAQ/{_howto,_example}
%dir %{_sysconfdir}/isdn
%config %{_sysconfdir}/isdn/*
%attr(755,root,root) %{_bindir}/[^c]*
%attr(755,root,root) %{_sbindir}/[^acr]*
%dir %{_libdir}/isdn
%{_libdir}/isdn/*
%dir /var/lock/isdn
%{_mandir}/man[1457]/*
%{_mandir}/man8/[^ac]*

%files x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_xbindir}/*
%{_xlibdir}/X11/app-defaults/XISDNLoad
%{_xmandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_xincludedir}/X11/bitmaps/*

%files -n capi-libs-static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files -n ppp-capiplugin
%defattr(644,root,root,755)
%doc pppdcapiplugin/{README,examples/*,peers/*}
%attr(755,root,root) %{_libdir}/pppd/%{ppp_ver}/*
%{_mandir}/man8/capiplugin*

%files -n capi-libs
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files -n capi-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*.h

%files -n capi-tools
%doc rcapid/README
%attr(755,root,root) %{_sbindir}/[ar]*
%attr(755,root,root) %{_bindir}/capiinfo
%{_mandir}/man8/avmcapi*
%{_mandir}/man8/capiinfo*

%files -n capi
%doc capiinit/capi.conf
%attr(755,root,root) %{_sbindir}/capiinit
