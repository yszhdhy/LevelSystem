package com.xc.example.service;

import com.xc.model.model.SysRole;
import com.xc.model.vo.AssginRoleVo;
import com.baomidou.mybatisplus.extension.service.IService;

import java.util.Map;

public interface SysRoleService extends IService<SysRole> {

    //1 查询所有角色 和 当前用户所属角色
    Map<String, Object> findRoleDataByUserId(Long userId);

    //2 为用户分配角色
    void doAssign(AssginRoleVo assginRoleVo);
}
