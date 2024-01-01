# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-brotlipy
Epoch: 100
Version: 0.7.0
Release: 1%{?dist}
Summary: Python binding to the Brotli library
License: MIT
URL: https://github.com/python-hyper/brotlipy/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: python-rpm-macros
BuildRequires: python3-cffi >= 1.0.0
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This library contains Python bindings for the reference Brotli
encoder/decoder, available here. This allows Python software to use the
Brotli compression algorithm directly from Python code.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-brotlipy
Summary: Python binding to the Brotli library
Requires: python3
Requires: python3-cffi >= 1.0.0
Provides: python3-brotlipy = %{epoch}:%{version}-%{release}
Provides: python3dist(brotlipy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-brotlipy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(brotlipy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-brotlipy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(brotlipy) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-brotlipy
This library contains Python bindings for the reference Brotli
encoder/decoder, available here. This allows Python software to use the
Brotli compression algorithm directly from Python code.

%files -n python%{python3_version_nodots}-brotlipy
%license LICENSE
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-brotlipy
Summary: Python binding to the Brotli library
Requires: python3
Requires: python3-cffi >= 1.0.0
Provides: python3-brotlipy = %{epoch}:%{version}-%{release}
Provides: python3dist(brotlipy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-brotlipy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(brotlipy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-brotlipy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(brotlipy) = %{epoch}:%{version}-%{release}

%description -n python3-brotlipy
This library contains Python bindings for the reference Brotli
encoder/decoder, available here. This allows Python software to use the
Brotli compression algorithm directly from Python code.

%files -n python3-brotlipy
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-brotlipy
Summary: Python binding to the Brotli library
Requires: python3
Requires: python3-cffi >= 1.0.0
Provides: python3-brotlipy = %{epoch}:%{version}-%{release}
Provides: python3dist(brotlipy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-brotlipy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(brotlipy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-brotlipy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(brotlipy) = %{epoch}:%{version}-%{release}

%description -n python3-brotlipy
This library contains Python bindings for the reference Brotli
encoder/decoder, available here. This allows Python software to use the
Brotli compression algorithm directly from Python code.

%files -n python3-brotlipy
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
