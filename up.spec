Summary:	Displays the uptime in a human readable format
Name:		up
Version:	0.3
Release:	%mkrel 12
License:	GPL
Group:		System/Base
URL:		http://www.burdell.org/up.php3
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
up displays the uptime of the system accounting for decades, years, weeks,
days, hours, and minutes.  It can output the uptime in its standard hardcore
format or the standard 'uptime' (that program that comes with procps) format
for quick comparisons with other systems.

%prep

%setup -n %{name}-%{version}

%build
gcc %{optflags} -o up up.c

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m755 up %{buildroot}%{_bindir}/
install -m644 up.1 %{buildroot}%{_mandir}/man1/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.3-12mdv2010.0
+ Revision: 434563
- rebuild
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.3-10mdv2009.0
+ Revision: 255173
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.3-8mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3-8mdv2008.0
+ Revision: 66686
- Import up



* Fri Jul 14 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3-8mdv2007.0
- rebuild

* Fri Jun 03 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-7mdk
- rebuild

* Sun May 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3-6mdk
- build release

* Thu Jan 16 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.3-5mdk
- build release

* Sun Aug  4 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.3-4mdk
- rebuilt with gcc-3.2

* Mon May 20 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.3-3mdk
- rebuilt with gcc3.1

* Sat Dec 22 2001 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.3-2mdk
- removed requires.

* Sat Dec  8 2001 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.3-1mdk
- initial cooker contrib.
