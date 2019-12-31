%define oname mechanize

Summary:	Stateful programmatic web browsing
Name:		python-%{oname}
Version:	0.4.5
Release:	1
License:	BSD
Group:		Development/Python
Url:		http://wwwsearch.sourceforge.net/mechanize/
Source0:	https://files.pythonhosted.org/packages/77/1b/7e4b644108e4e99b136e52c6aae34873fcd267e3d2489f3bd2cff8655a59/mechanize-0.4.5.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
%rename		python-%oname

%description
Stateful programmatic web browsing, after Andy Lester's Perl module
WWW::Mechanize.

The library is layered:	mechanize.Browser (stateful web browser),
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
%setup -qn %{oname}-%{version}

%build
%py_build

%install
%py_install

%files
%{py_puresitedir}/%{oname}*

