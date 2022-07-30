// Licensed to the .NET Foundation under one or more agreements.
// The .NET Foundation licenses this file to you under the MIT license.
// See the LICENSE file in the project root for more information.

using System;

namespace System.Runtime.InteropServices
{
    /// <summary>
    ///     The McgPInvokeMarshalStubAttribute is generated by MCG to indicate what is exact method that this
    ///     particular P/Invoke is for.
    ///
    ///     For example, user could write [DllImport] Program.MyFunc. MCG will import this P/Invoke and will
    ///     generate another function with the real marshalling code which has this attribute that tells us
    ///     what the user P/invoke really is. And our PInvokeTransform will take care of injecting the MCG
    ///     generated function body into the user P/invoke.
    /// </summary>
    [AttributeUsage(AttributeTargets.Method, AllowMultiple = false, Inherited = false)]
    public sealed class McgPInvokeMarshalStubAttribute : Attribute
    {
        public McgPInvokeMarshalStubAttribute(string assemblyName, string typeName, string methodName)
        {
        }
    }
}