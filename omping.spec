Name: omping
Version: 0.0.1
Release: 4%{?dist}
Summary: Utility to test IP multicast functionality
Group: Applications/Internet
License: ISC
URL: http://fedorahosted.org/omping/
Source0: http://fedorahosted.org/releases/o/m/omping/%{name}-%{version}.tar.gz
Patch0: omping-001-one-host-specified.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Omping (Open Multicast Ping) is tool to test IP multicast functionality
primarily in local network.

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
make DESTDIR="%{buildroot}" PREFIX="%{_prefix}" install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/%{name}
%{_mandir}/man8/*

%changelog
* Tue Dec 07 2010 Jan Friesse <jfriesse@redhat.com> - 0.0.1-4
- Initial RHEL-6 build (#657370).

* Tue Nov 30 2010 Jan Friesse <jfriesse@redhat.com> - 0.0.1-3
- Display error if only one host is specified

* Wed Nov 24 2010 Jan Friesse <jfriesse@redhat.com> - 0.0.1-2
- Change hard coded prefix path to macro

* Fri Nov 19 2010 Jan Friesse <jfriesse@redhat.com> - 0.0.1-1
- Initial package for Fedora
