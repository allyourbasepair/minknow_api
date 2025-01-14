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

// MinionDeviceServiceClient is the client API for MinionDeviceService service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type MinionDeviceServiceClient interface {
	// Change the settings for the active device.
	//
	// If you omit a parameter, that setting will not be changed.
	//
	// This call is atomic: either all the settings will be applied, or none of them (if there is an
	// error).
	ChangeSettings(ctx context.Context, in *ChangeSettingsRequest, opts ...grpc.CallOption) (*ChangeSettingsResponse, error)
	// Get the current settings for the active device.
	GetSettings(ctx context.Context, in *GetSettingsRequest, opts ...grpc.CallOption) (*GetSettingsResponse, error)
	// Get the rotational rate of the fan cooling the heat-sink. (Not available
	// on all MinION platforms.)
	GetFanSpeed(ctx context.Context, in *GetFanSpeedRequest, opts ...grpc.CallOption) (*GetFanSpeedResponse, error)
}

type minionDeviceServiceClient struct {
	cc grpc.ClientConnInterface
}

func NewMinionDeviceServiceClient(cc grpc.ClientConnInterface) MinionDeviceServiceClient {
	return &minionDeviceServiceClient{cc}
}

func (c *minionDeviceServiceClient) ChangeSettings(ctx context.Context, in *ChangeSettingsRequest, opts ...grpc.CallOption) (*ChangeSettingsResponse, error) {
	out := new(ChangeSettingsResponse)
	err := c.cc.Invoke(ctx, "/minknow_api.minion_device.MinionDeviceService/change_settings", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *minionDeviceServiceClient) GetSettings(ctx context.Context, in *GetSettingsRequest, opts ...grpc.CallOption) (*GetSettingsResponse, error) {
	out := new(GetSettingsResponse)
	err := c.cc.Invoke(ctx, "/minknow_api.minion_device.MinionDeviceService/get_settings", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *minionDeviceServiceClient) GetFanSpeed(ctx context.Context, in *GetFanSpeedRequest, opts ...grpc.CallOption) (*GetFanSpeedResponse, error) {
	out := new(GetFanSpeedResponse)
	err := c.cc.Invoke(ctx, "/minknow_api.minion_device.MinionDeviceService/get_fan_speed", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// MinionDeviceServiceServer is the server API for MinionDeviceService service.
// All implementations must embed UnimplementedMinionDeviceServiceServer
// for forward compatibility
type MinionDeviceServiceServer interface {
	// Change the settings for the active device.
	//
	// If you omit a parameter, that setting will not be changed.
	//
	// This call is atomic: either all the settings will be applied, or none of them (if there is an
	// error).
	ChangeSettings(context.Context, *ChangeSettingsRequest) (*ChangeSettingsResponse, error)
	// Get the current settings for the active device.
	GetSettings(context.Context, *GetSettingsRequest) (*GetSettingsResponse, error)
	// Get the rotational rate of the fan cooling the heat-sink. (Not available
	// on all MinION platforms.)
	GetFanSpeed(context.Context, *GetFanSpeedRequest) (*GetFanSpeedResponse, error)
	mustEmbedUnimplementedMinionDeviceServiceServer()
}

// UnimplementedMinionDeviceServiceServer must be embedded to have forward compatible implementations.
type UnimplementedMinionDeviceServiceServer struct {
}

func (UnimplementedMinionDeviceServiceServer) ChangeSettings(context.Context, *ChangeSettingsRequest) (*ChangeSettingsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ChangeSettings not implemented")
}
func (UnimplementedMinionDeviceServiceServer) GetSettings(context.Context, *GetSettingsRequest) (*GetSettingsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetSettings not implemented")
}
func (UnimplementedMinionDeviceServiceServer) GetFanSpeed(context.Context, *GetFanSpeedRequest) (*GetFanSpeedResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetFanSpeed not implemented")
}
func (UnimplementedMinionDeviceServiceServer) mustEmbedUnimplementedMinionDeviceServiceServer() {}

// UnsafeMinionDeviceServiceServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to MinionDeviceServiceServer will
// result in compilation errors.
type UnsafeMinionDeviceServiceServer interface {
	mustEmbedUnimplementedMinionDeviceServiceServer()
}

func RegisterMinionDeviceServiceServer(s grpc.ServiceRegistrar, srv MinionDeviceServiceServer) {
	s.RegisterService(&MinionDeviceService_ServiceDesc, srv)
}

func _MinionDeviceService_ChangeSettings_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ChangeSettingsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MinionDeviceServiceServer).ChangeSettings(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/minknow_api.minion_device.MinionDeviceService/change_settings",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MinionDeviceServiceServer).ChangeSettings(ctx, req.(*ChangeSettingsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _MinionDeviceService_GetSettings_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetSettingsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MinionDeviceServiceServer).GetSettings(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/minknow_api.minion_device.MinionDeviceService/get_settings",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MinionDeviceServiceServer).GetSettings(ctx, req.(*GetSettingsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _MinionDeviceService_GetFanSpeed_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(GetFanSpeedRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MinionDeviceServiceServer).GetFanSpeed(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/minknow_api.minion_device.MinionDeviceService/get_fan_speed",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MinionDeviceServiceServer).GetFanSpeed(ctx, req.(*GetFanSpeedRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// MinionDeviceService_ServiceDesc is the grpc.ServiceDesc for MinionDeviceService service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var MinionDeviceService_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "minknow_api.minion_device.MinionDeviceService",
	HandlerType: (*MinionDeviceServiceServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "change_settings",
			Handler:    _MinionDeviceService_ChangeSettings_Handler,
		},
		{
			MethodName: "get_settings",
			Handler:    _MinionDeviceService_GetSettings_Handler,
		},
		{
			MethodName: "get_fan_speed",
			Handler:    _MinionDeviceService_GetFanSpeed_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "minknow_api/minion_device.proto",
}
