Summary:	Utilities for the kernel ISDN-subsystem
Summary(pl):	U¿ytki dla podsystemu ISDN j±dra
Name:		isdn4k-utils
Version:	0112071200
Release:	3
License:	distributable
Group:		Applications/Communications
Source0:	%{name}-%{version}.tar.gz
Source1:        %{name}.config
Patch0:         %{name}-Makefiles.patch
URL:		http://www.franken.de/ftp/pub/isdn4linux/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Utilities for the kernel ISDN-subsystem and some contributions.
%description -l pl
U¿ytki dla podsystemu ISDN j±dra.

%prep
%setup0 -q
%patch0 -p1



%build
cp %{SOURCE1} .config
%{__make} OPTIM="%{rpmcflags}" subconfig
%{__make} CFLAGS="%{rpmcflags}"



%install
rm -rf $RPM_BUILD_ROOT

#%{__make} devices

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/isdn,%{_sbindir},%{_bindir},/var/lock/isdn,%{_libdir},%{_includedir}} $RPM_BUILD_ROOT{/usr/X11R6/lib/X11/app-defaults} $RPM_BUILD_ROOT%{_mandir}/{man1,man2,man3,man4,man5,man6,man7,man8}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

#install isdnlog/isdnrep/isdnrep.1 $RPM_BUILD_ROOT%{_mandir}/man1
#install isdnlog/isdnlog/isdnlog.8 $RPM_BUILD_ROOT%{_mandir}/man8
#echo ".so ttyI.4" > $RPM_BUILD_ROOT%{_mandir}/man4/cui.4

gzip -9nf COPYING README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.gz README.gz 
%dir /var/lock/isdn

%dir %{_sysconfdir}/isdn
%config %{_sysconfdir}/isdn/*


%attr(755,root,root) %{_sbindir}/*

/usr/X11R6/lib/X11/app-defaults/XISDNLoad

%attr(755,root,root) %{_bindir}/*


#%dir %{_libdir}/isdn
%{_libdir}/*

#%{_libdir}/isdn/*
#%{_libdir}/vbox

%{_mandir}/*
