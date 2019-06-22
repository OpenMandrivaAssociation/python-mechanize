%define oname mechanize

Summary:	Stateful programmatic web browsing
Name:		python2-%{oname}
Version:	0.4.2
Release:	13
License:	BSD
Group:		Development/Python
Url:		http://wwwsearch.sourceforge.net/mechanize/
Source0:	https://files.pythonhosted.org/packages/79/6b/c256ffe2abd560a2857bd66131e01ddfb4b123510a0100a495ded8f191cc/mechanize-0.4.2.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
Requires:	python-clientform
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

