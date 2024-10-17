Name:		texlive-gettitlestring
Version:	53170
Release:	2
Summary:	Clean up title references
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gettitlestring
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gettitlestring.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gettitlestring.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gettitlestring.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Cleans up the title string (removing \label commands) for
packages (such as nameref) that typeset such strings.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/gettitlestring
%{_texmfdistdir}/tex/generic/gettitlestring
%doc %{_texmfdistdir}/doc/latex/gettitlestring

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
