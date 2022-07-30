// Licensed to the .NET Foundation under one or more agreements.
// The .NET Foundation licenses this file to you under the MIT license.
// See the LICENSE file in the project root for more information.

using System;

namespace System.Reflection
{
    /// <summary>
    /// A record for dispatch proxies that maps an interface type and proxy class type to a proxy
    /// instance class type that was generated by the toolchain at compile-time.
    /// </summary>
    public struct DispatchProxyEntry
    {
        public RuntimeTypeHandle ProxyClassType { get; set; }
        public RuntimeTypeHandle InterfaceType { get; set; }
        public RuntimeTypeHandle ImplementationClassType { get; set; }
    }
}