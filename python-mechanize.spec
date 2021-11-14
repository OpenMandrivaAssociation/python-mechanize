%define oname mechanize

Summary:	Stateful programmatic web browsing
Name:		python-%{oname}
Version:	0.4.7
Release:	1
License:	BSD
Group:		Development/Python
Url:		http://wwwsearch.sourceforge.net/mechanize/
Source0:	https://files.pythonhosted.org/packages/b0/12/2226549e042be8f2f4dddd3b4a44973e7bacd229f857299f33bde3f77e9d/mechanize-0.4.7.tar.gz
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

