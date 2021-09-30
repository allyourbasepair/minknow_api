// Code generated by protoc-gen-go-grpc. DO NOT EDIT.

package minknow

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// BasecallerClient is the client API for Basecaller service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type BasecallerClient interface {
	// List the available basecalling configurations sorted by flow cell and kit.
	//
	// Since 3.5
	ListConfigsByKit(ctx context.Context, in *ListConfigsByKitRequest, opts ...grpc.CallOption) (*ListConfigsByKitResponse, error)
	// Start basecalling reads files.
	//
	// Since 4.0
	StartBasecalling(ctx context.Context, in *StartBasecallingRequest, opts ...grpc.CallOption) (*StartBasecallingResponse, error)
	// Start barcoding fastq files.
	//
	// Since 3.8
	StartBarcoding(ctx context.Context, in *StartBarcodingRequest, opts ...grpc.CallOption) (*StartBarcodingResponse, error)
	// Start aligning fastq files.
	//
	// Since 3.8
	StartAlignment(ctx context.Context, in *StartAlignmentRequest, opts ...grpc.CallOption) (*StartAlignmentResponse, error)
	// Stop a basecalling that was started by start_basecalling_reads().
	//
	// Since 3.5
	Cancel(ctx context.Context, in *CancelRequest, opts ...grpc.CallOption) (*CancelResponse, error)
	// Gets information about one or more basecalling operations.
	//
	// Since 3.5
	GetInfo(ctx context.Context, in *GetInfoRequest, opts ...grpc.CallOption) (Basecaller_GetInfoClient, error)
	// Monitors basecalls, returning messages when basecalls are started, stopped or receive
	// progress updates.
	//
	// The current state of all currently-running basecalls will be returned in the initial set of
	// messages. Optionally, the state of all already-finished runs can be included. Note that this
	// initial state may be split among several responses.
	//
	// Note that progress updates may be rate limited to avoid affecting performance.
	//
	// Since 3.5
	Watch(ctx context.Context, in *WatchRequest, opts ...grpc.CallOption) (Basecaller_WatchClient, error)
	// Build an alignment index file from an input fasta reference.
	//
	// This call blocks whilst the index is built.
	//
	// Since 4.3
	MakeAlignmentIndex(ctx context.Context, in *MakeAlignmentIndexRequest, opts ...grpc.CallOption) (*MakeAlignmentIndexResponse, error)
}

type basecallerClient struct {
	cc grpc.ClientConnInterface
}

func NewBasecallerClient(cc grpc.ClientConnInterface) BasecallerClient {
	return &basecallerClient{cc}
}

func (c *basecallerClient) ListConfigsByKit(ctx context.Context, in *ListConfigsByKitRequest, opts ...grpc.CallOption) (*ListConfigsByKitResponse, error) {
	out := new(ListConfigsByKitResponse)
	err := c.cc.Invoke(ctx, "/minknow_api.basecaller.Basecaller/list_configs_by_kit", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *basecallerClient) StartBasecalling(ctx context.Context, in *StartBasecallingRequest, opts ...grpc.CallOption) (*StartBasecallingResponse, error) {
	out := new(StartBasecallingResponse)
	err := c.cc.Invoke(ctx, "/minknow_api.basecaller.Basecaller/start_basecalling", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *basecallerClient) StartBarcoding(ctx context.Context, in *StartBarcodingRequest, opts ...grpc.CallOption) (*StartBarcodingResponse, error) {
	out := new(StartBarcodingResponse)
	err := c.cc.Invoke(ctx, "/minknow_api.basecaller.Basecaller/start_barcoding", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *basecallerClient) StartAlignment(ctx context.Context, in *StartAlignmentRequest, opts ...grpc.CallOption) (*StartAlignmentResponse, error) {
	out := new(StartAlignmentResponse)
	err := c.cc.Invoke(ctx, "/minknow_api.basecaller.Basecaller/start_alignment", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *basecallerClient) Cancel(ctx context.Context, in *CancelRequest, opts ...grpc.CallOption) (*CancelResponse, error) {
	out := new(CancelResponse)
	err := c.cc.Invoke(ctx, "/minknow_api.basecaller.Basecaller/cancel", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *basecallerClient) GetInfo(ctx context.Context, in *GetInfoRequest, opts ...grpc.CallOption) (Basecaller_GetInfoClient, error) {
	stream, err := c.cc.NewStream(ctx, &Basecaller_ServiceDesc.Streams[0], "/minknow_api.basecaller.Basecaller/get_info", opts...)
	if err != nil {
		return nil, err
	}
	x := &basecallerGetInfoClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type Basecaller_GetInfoClient interface {
	Recv() (*GetInfoResponse, error)
	grpc.ClientStream
}

type basecallerGetInfoClient struct {
	grpc.ClientStream
}

func (x *basecallerGetInfoClient) Recv() (*GetInfoResponse, error) {
	m := new(GetInfoResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *basecallerClient) Watch(ctx context.Context, in *WatchRequest, opts ...grpc.CallOption) (Basecaller_WatchClient, error) {
	stream, err := c.cc.NewStream(ctx, &Basecaller_ServiceDesc.Streams[1], "/minknow_api.basecaller.Basecaller/watch", opts...)
	if err != nil {
		return nil, err
	}
	x := &basecallerWatchClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type Basecaller_WatchClient interface {
	Recv() (*WatchResponse, error)
	grpc.ClientStream
}

type basecallerWatchClient struct {
	grpc.ClientStream
}

func (x *basecallerWatchClient) Recv() (*WatchResponse, error) {
	m := new(WatchResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *basecallerClient) MakeAlignmentIndex(ctx context.Context, in *MakeAlignmentIndexRequest, opts ...grpc.CallOption) (*MakeAlignmentIndexResponse, error) {
	out := new(MakeAlignmentIndexResponse)
	err := c.cc.Invoke(ctx, "/minknow_api.basecaller.Basecaller/make_alignment_index", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// BasecallerServer is the server API for Basecaller service.
// All implementations must embed UnimplementedBasecallerServer
// for forward compatibility
type BasecallerServer interface {
	// List the available basecalling configurations sorted by flow cell and kit.
	//
	// Since 3.5
	ListConfigsByKit(context.Context, *ListConfigsByKitRequest) (*ListConfigsByKitResponse, error)
	// Start basecalling reads files.
	//
	// Since 4.0
	StartBasecalling(context.Context, *StartBasecallingRequest) (*StartBasecallingResponse, error)
	// Start barcoding fastq files.
	//
	// Since 3.8
	StartBarcoding(context.Context, *StartBarcodingRequest) (*StartBarcodingResponse, error)
	// Start aligning fastq files.
	//
	// Since 3.8
	StartAlignment(context.Context, *StartAlignmentRequest) (*StartAlignmentResponse, error)
	// Stop a basecalling that was started by start_basecalling_reads().
	//
	// Since 3.5
	Cancel(context.Context, *CancelRequest) (*CancelResponse, error)
	// Gets information about one or more basecalling operations.
	//
	// Since 3.5
	GetInfo(*GetInfoRequest, Basecaller_GetInfoServer) error
	// Monitors basecalls, returning messages when basecalls are started, stopped or receive
	// progress updates.
	//
	// The current state of all currently-running basecalls will be returned in the initial set of
	// messages. Optionally, the state of all already-finished runs can be included. Note that this
	// initial state may be split among several responses.
	//
	// Note that progress updates may be rate limited to avoid affecting performance.
	//
	// Since 3.5
	Watch(*WatchRequest, Basecaller_WatchServer) error
	// Build an alignment index file from an input fasta reference.
	//
	// This call blocks whilst the index is built.
	//
	// Since 4.3
	MakeAlignmentIndex(context.Context, *MakeAlignmentIndexRequest) (*MakeAlignmentIndexResponse, error)
	mustEmbedUnimplementedBasecallerServer()
}

// UnimplementedBasecallerServer must be embedded to have forward compatible implementations.
type UnimplementedBasecallerServer struct {
}

func (UnimplementedBasecallerServer) ListConfigsByKit(context.Context, *ListConfigsByKitRequest) (*ListConfigsByKitResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListConfigsByKit not implemented")
}
func (UnimplementedBasecallerServer) StartBasecalling(context.Context, *StartBasecallingRequest) (*StartBasecallingResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method StartBasecalling not implemented")
}
func (UnimplementedBasecallerServer) StartBarcoding(context.Context, *StartBarcodingRequest) (*StartBarcodingResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method StartBarcoding not implemented")
}
func (UnimplementedBasecallerServer) StartAlignment(context.Context, *StartAlignmentRequest) (*StartAlignmentResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method StartAlignment not implemented")
}
func (UnimplementedBasecallerServer) Cancel(context.Context, *CancelRequest) (*CancelResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method Cancel not implemented")
}
func (UnimplementedBasecallerServer) GetInfo(*GetInfoRequest, Basecaller_GetInfoServer) error {
	return status.Errorf(codes.Unimplemented, "method GetInfo not implemented")
}
func (UnimplementedBasecallerServer) Watch(*WatchRequest, Basecaller_WatchServer) error {
	return status.Errorf(codes.Unimplemented, "method Watch not implemented")
}
func (UnimplementedBasecallerServer) MakeAlignmentIndex(context.Context, *MakeAlignmentIndexRequest) (*MakeAlignmentIndexResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method MakeAlignmentIndex not implemented")
}
func (UnimplementedBasecallerServer) mustEmbedUnimplementedBasecallerServer() {}

// UnsafeBasecallerServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to BasecallerServer will
// result in compilation errors.
type UnsafeBasecallerServer interface {
	mustEmbedUnimplementedBasecallerServer()
}

func RegisterBasecallerServer(s grpc.ServiceRegistrar, srv BasecallerServer) {
	s.RegisterService(&Basecaller_ServiceDesc, srv)
}

func _Basecaller_ListConfigsByKit_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ListConfigsByKitRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BasecallerServer).ListConfigsByKit(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/minknow_api.basecaller.Basecaller/list_configs_by_kit",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BasecallerServer).ListConfigsByKit(ctx, req.(*ListConfigsByKitRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Basecaller_StartBasecalling_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(StartBasecallingRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BasecallerServer).StartBasecalling(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/minknow_api.basecaller.Basecaller/start_basecalling",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BasecallerServer).StartBasecalling(ctx, req.(*StartBasecallingRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Basecaller_StartBarcoding_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(StartBarcodingRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BasecallerServer).StartBarcoding(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/minknow_api.basecaller.Basecaller/start_barcoding",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BasecallerServer).StartBarcoding(ctx, req.(*StartBarcodingRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Basecaller_StartAlignment_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(StartAlignmentRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BasecallerServer).StartAlignment(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/minknow_api.basecaller.Basecaller/start_alignment",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BasecallerServer).StartAlignment(ctx, req.(*StartAlignmentRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Basecaller_Cancel_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(CancelRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BasecallerServer).Cancel(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/minknow_api.basecaller.Basecaller/cancel",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BasecallerServer).Cancel(ctx, req.(*CancelRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Basecaller_GetInfo_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(GetInfoRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(BasecallerServer).GetInfo(m, &basecallerGetInfoServer{stream})
}

type Basecaller_GetInfoServer interface {
	Send(*GetInfoResponse) error
	grpc.ServerStream
}

type basecallerGetInfoServer struct {
	grpc.ServerStream
}

func (x *basecallerGetInfoServer) Send(m *GetInfoResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _Basecaller_Watch_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(WatchRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(BasecallerServer).Watch(m, &basecallerWatchServer{stream})
}

type Basecaller_WatchServer interface {
	Send(*WatchResponse) error
	grpc.ServerStream
}

type basecallerWatchServer struct {
	grpc.ServerStream
}

func (x *basecallerWatchServer) Send(m *WatchResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _Basecaller_MakeAlignmentIndex_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(MakeAlignmentIndexRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BasecallerServer).MakeAlignmentIndex(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/minknow_api.basecaller.Basecaller/make_alignment_index",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BasecallerServer).MakeAlignmentIndex(ctx, req.(*MakeAlignmentIndexRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Basecaller_ServiceDesc is the grpc.ServiceDesc for Basecaller service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Basecaller_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "minknow_api.basecaller.Basecaller",
	HandlerType: (*BasecallerServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "list_configs_by_kit",
			Handler:    _Basecaller_ListConfigsByKit_Handler,
		},
		{
			MethodName: "start_basecalling",
			Handler:    _Basecaller_StartBasecalling_Handler,
		},
		{
			MethodName: "start_barcoding",
			Handler:    _Basecaller_StartBarcoding_Handler,
		},
		{
			MethodName: "start_alignment",
			Handler:    _Basecaller_StartAlignment_Handler,
		},
		{
			MethodName: "cancel",
			Handler:    _Basecaller_Cancel_Handler,
		},
		{
			MethodName: "make_alignment_index",
			Handler:    _Basecaller_MakeAlignmentIndex_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "get_info",
			Handler:       _Basecaller_GetInfo_Handler,
			ServerStreams: true,
		},
		{
			StreamName:    "watch",
			Handler:       _Basecaller_Watch_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "minknow_api/basecaller.proto",
}