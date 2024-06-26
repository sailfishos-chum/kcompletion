%global kf5_version 5.116.0
%global framework kcompletion

Name: 			opt-kf5-kcompletion
Version: 5.116.0
Release: 		1%{?dist}
Summary:        KDE Frameworks 5 Tier 2 addon with auto completion widgets and classes

License:        LGPLv2+
URL:            https://invent.kde.org/frameworks/%{framework}
Source0: 		%{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

## upstream fixes

BuildRequires:  opt-extra-cmake-modules >= %{kf5_version}
BuildRequires:  opt-kf5-rpm-macros >= %{kf5_version}
BuildRequires:  opt-kf5-kconfig-devel 
BuildRequires:  opt-kf5-kwidgetsaddons-devel
BuildRequires:  opt-qt5-qtbase-devel
BuildRequires:  opt-qt5-qttools-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtbase-gui

%description
KCompletion provides widgets with advanced completion support as well as a
lower-level completion class which can be used with your own widgets.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opt-qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%_opt_cmake_kf5
%cmake_build

%install
%cmake_install

%find_lang_kf5 kcompletion5_qt

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files

%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_datadir}/locale/
%{_opt_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_opt_kf5_libdir}/libKF5Completion.so.*
%{_opt_kf5_qtplugindir}/designer/*5widgets.so

%files devel

%{_opt_kf5_includedir}/KF5/KCompletion/
%{_opt_kf5_libdir}/libKF5Completion.so
%{_opt_kf5_libdir}/cmake/KF5Completion/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KCompletion.pri

