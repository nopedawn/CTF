package com.bcactf.flagtureiser;

import java.util.Collections;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.item.Item;
import net.minecraftforge.common.ForgeConfigSpec;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.Mod.EventBusSubscriber;
import net.minecraftforge.fml.event.config.ModConfigEvent;
import net.minecraftforge.registries.ForgeRegistries;

@EventBusSubscriber(modid = "flagtureiser", bus = Mod.EventBusSubscriber.Bus.MOD)
public class Config {
  private static final ForgeConfigSpec.Builder BUILDER = new ForgeConfigSpec.Builder();
  
  private static final ForgeConfigSpec.BooleanValue LOG_DIRT_BLOCK = BUILDER
    .comment("Whether to log the dirt block on common setup")
    .define("logDirtBlock", true);
  
  private static final ForgeConfigSpec.IntValue MAGIC_NUMBER = BUILDER
    .comment("A magic number")
    .defineInRange("magicNumber", 42, 0, 2147483647);
  
  public static final ForgeConfigSpec.ConfigValue<String> MAGIC_NUMBER_INTRODUCTION = BUILDER
    .comment("What you want the introduction message to be for the magic number")
    .define("magicNumberIntroduction", "The magic number is... ");
  
  private static final ForgeConfigSpec.ConfigValue<List<? extends String>> ITEM_STRINGS = BUILDER
    .comment("A list of items to log on common setup.")
    .defineListAllowEmpty(Collections.singletonList("items"), () -> List.of("minecraft:iron_ingot"), Config::validateItemName);
  
  static final ForgeConfigSpec SPEC = BUILDER.build();
  
  public static boolean logDirtBlock;
  
  public static int magicNumber;
  
  public static String magicNumberIntroduction;
  
  public static Set<Item> items;
  
  private static boolean validateItemName(Object obj) {
    String itemName = (String)obj;
    return (obj instanceof String && ForgeRegistries.ITEMS.containsKey(new ResourceLocation(itemName)));
  }
  
  @SubscribeEvent
  static void onLoad(ModConfigEvent event) {
    logDirtBlock = ((Boolean)LOG_DIRT_BLOCK.get()).booleanValue();
    magicNumber = ((Integer)MAGIC_NUMBER.get()).intValue();
    magicNumberIntroduction = (String)MAGIC_NUMBER_INTRODUCTION.get();
    items = (Set<Item>)((List)ITEM_STRINGS.get()).stream().map(itemName -> (Item)ForgeRegistries.ITEMS.getValue(new ResourceLocation(itemName))).collect(Collectors.toSet());
  }
}
