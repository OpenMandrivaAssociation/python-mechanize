%define oname mechanize

Summary:	Stateful programmatic web browsing
Name:		python-%{oname}
Version:	0.2.5
Release:	4
Source0:	http://wwwsearch.sourceforge.net/%oname/src/%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
URL:		http://wwwsearch.sourceforge.net/mechanize/
BuildRequires:	python-devel
BuildRequires:	python-setuptools
Requires:	python-clientform
Obsoletes:	python-clientcookie < 1.3.0-2
Provides:	python-clientcookie

%description
Stateful programmatic web browsing, after Andy Lester's Perl module
WWW::Mechanize.

The library is layered: mechanize.Browser (stateful web browser),
mechanize.UserAgent (configurable URL opener), plus urllib2 handlers.

Features include: ftp:, http: and file: URL schemes, browser history,
high-level hyperlink and HTML form support, HTTP cookies, HTTP-EQUIV and
Refresh, Referer [sic] header, robots.txt, redirections, proxies, and
Basic and Digest HTTP authentication.  mechanize's response objects are
(lazily-) .seek()able and still work after .close().

Much of the code originally derived from Perl code by Gisle Aas
(libwww-perl), Johnny Lee (MSIE Cookie support) and last but not least
Andy Lester (WWW::Mechanize).  urllib2 was written by Jeremy Hylton.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --single-version-externally-managed --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/* *.txt
%{py_puresitedir}/%{oname}*



%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.5-2mdv2011.0
+ Revision: 668001
- mass rebuild

* Fri Apr 01 2011 Götz Waschk <waschk@mandriva.org> 0.2.5-1
+ Revision: 649583
- update to new version 0.2.5

* Fri Oct 29 2010 Götz Waschk <waschk@mandriva.org> 0.2.4-1mdv2011.0
+ Revision: 589922
- update to new version 0.2.4

* Sun Oct 17 2010 Götz Waschk <waschk@mandriva.org> 0.2.3-1mdv2011.0
+ Revision: 586250
- update to new version 0.2.3

* Mon Jul 19 2010 Götz Waschk <waschk@mandriva.org> 0.2.2-1mdv2011.0
+ Revision: 554907
- update to new version 0.2.2

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 0.2.1-1mdv2011.0
+ Revision: 550284
- update to new version 0.2.1

* Fri Apr 23 2010 Götz Waschk <waschk@mandriva.org> 0.2.0-1mdv2010.1
+ Revision: 538140
- new version
- update docs list

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.11-2mdv2010.1
+ Revision: 523829
- rebuilt for 2010.1

* Mon Jun 08 2009 Götz Waschk <waschk@mandriva.org> 0.1.11-1mdv2010.0
+ Revision: 383904
- new version
- fix source URL

* Mon Dec 29 2008 Adam Williamson <awilliamson@mandriva.org> 0.1.10-2mdv2009.1
+ Revision: 320810
- clean up the clientcookie obsolete / provide

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 0.1.10-1mdv2009.1
+ Revision: 319215
- buildrequires python-setuptools
- rebuild with python 2.6
- obsolete python-clientcookie
- clean spec a bit
- new release 0.1.10

* Sun Jul 27 2008 Götz Waschk <waschk@mandriva.org> 0.1.7b-2mdv2009.0
+ Revision: 250656
- add docs
- update deps

* Sun Jul 27 2008 Götz Waschk <waschk@mandriva.org> 0.1.7b-1mdv2009.0
+ Revision: 250619
- import python-mechanize


