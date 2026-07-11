%global tl_name gettitlestring
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Clean up title references
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gettitlestring
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gettitlestring.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gettitlestring.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gettitlestring.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Cleans up the title string (removing \label commands) for packages (such
as nameref) that typeset such strings.

